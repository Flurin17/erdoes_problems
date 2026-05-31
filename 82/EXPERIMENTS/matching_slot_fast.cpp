// Exact checker for the first-lift matching-slot target on small even graphs.
//
// It enumerates labelled even graphs by choosing all edges not incident with
// the last vertex and then adding the unique parity-correction edges to the
// last vertex.  The target is a partition into slots (0,0,1,2) modulo 4, with
// every residue-1 part required to be exactly 1-regular.

#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

namespace {

int edge_index(int n, int a, int b) {
    if (a > b) std::swap(a, b);
    int idx = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (i == a && j == b) return idx;
            ++idx;
        }
    }
    return -1;
}

int state_code(const std::array<int, 4>& counts) {
    int code = 0;
    int pow5 = 1;
    for (int r = 0; r < 4; ++r) {
        code += counts[r] * pow5;
        pow5 *= 5;
    }
    return code;
}

bool has_count(int code, int residue) {
    for (int i = 0; i < residue; ++i) code /= 5;
    return code % 5;
}

int remove_count(int code, int residue) {
    int pow5 = 1;
    for (int i = 0; i < residue; ++i) pow5 *= 5;
    return code - pow5;
}

class Checker {
  public:
    explicit Checker(int n_value)
        : n(n_value),
          full((1 << n_value) - 1),
          incident(1 << n_value),
          submasks_with_pivot(1 << n_value) {
        for (int subset = 1; subset <= full; ++subset) {
            for (int v = 0; v < n; ++v) {
                if (!((subset >> v) & 1)) continue;
                uint64_t mask = 0;
                for (int w = 0; w < n; ++w) {
                    if (v == w || !((subset >> w) & 1)) continue;
                    mask |= uint64_t{1} << edge_index(n, v, w);
                }
                incident[subset][v] = mask;
            }
        }
        for (int remaining = 1; remaining <= full; ++remaining) {
            int pivot = remaining & -remaining;
            for (int sub = remaining; sub; sub = (sub - 1) & remaining) {
                if (sub & pivot) submasks_with_pivot[remaining].push_back(sub);
            }
        }
    }

    void compute_valid_subsets(uint64_t graph_mask) {
        residue.fill(-1);
        exact_matching.fill(false);
        for (int subset = 1; subset <= full; ++subset) {
            int first = __builtin_ctz(static_cast<unsigned>(subset));
            int first_degree =
                __builtin_popcountll(graph_mask & incident[subset][first]);
            int value = first_degree % 4;
            bool modular = true;
            bool matching = first_degree == 1;
            int rest = subset & ~(1 << first);
            while (rest) {
                int bit = rest & -rest;
                int v = __builtin_ctz(static_cast<unsigned>(bit));
                int degree = __builtin_popcountll(graph_mask & incident[subset][v]);
                if (degree % 4 != value) {
                    modular = false;
                    break;
                }
                if (degree != 1) matching = false;
                rest ^= bit;
            }
            if (modular) {
                residue[subset] = value;
                exact_matching[subset] = matching;
            }
        }
    }

    bool has_partition() {
        for (auto& row : memo) row.fill(-1);
        std::array<int, 4> counts{2, 1, 1, 0};
        return rec(full, state_code(counts));
    }

  private:
    int n;
    int full;
    std::vector<std::array<uint64_t, 10>> incident;
    std::vector<std::vector<int>> submasks_with_pivot;
    std::array<int, 1 << 10> residue{};
    std::array<bool, 1 << 10> exact_matching{};
    std::array<std::array<int8_t, 625>, 1 << 10> memo{};

    bool rec(int remaining, int code) {
        if (remaining == 0) return true;
        if (code == 0) return false;
        int8_t& saved = memo[remaining][code];
        if (saved != -1) return saved;
        for (int r = 0; r < 3; ++r) {
            if (!has_count(code, r)) continue;
            int next_code = remove_count(code, r);
            for (int sub : submasks_with_pivot[remaining]) {
                if (residue[sub] != r) continue;
                if (r == 1 && !exact_matching[sub]) continue;
                if (rec(remaining ^ sub, next_code)) {
                    saved = 1;
                    return true;
                }
            }
        }
        saved = 0;
        return false;
    }
};

uint64_t even_graph_mask(int n, uint64_t bits) {
    uint64_t graph_mask = 0;
    std::array<int, 10> parity{};
    int bit_index = 0;
    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n - 1; ++j) {
            if ((bits >> bit_index) & 1) {
                int idx = edge_index(n, i, j);
                graph_mask |= uint64_t{1} << idx;
                parity[i] ^= 1;
                parity[j] ^= 1;
            }
            ++bit_index;
        }
    }
    for (int i = 0; i < n - 1; ++i) {
        if (parity[i]) {
            int idx = edge_index(n, i, n - 1);
            graph_mask |= uint64_t{1} << idx;
            parity[n - 1] ^= 1;
        }
    }
    return graph_mask;
}

}  // namespace

int main(int argc, char** argv) {
    int n = 8;
    uint64_t limit = 0;
    bool progress = false;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--n" && i + 1 < argc) {
            n = std::stoi(argv[++i]);
        } else if (arg == "--limit" && i + 1 < argc) {
            limit = std::stoull(argv[++i]);
        } else if (arg == "--progress") {
            progress = true;
        } else {
            std::cerr << "usage: matching_slot_fast [--n N] [--limit L] [--progress]\n";
            return 2;
        }
    }
    if (n < 1 || n > 10) {
        std::cerr << "supported range: 1 <= n <= 10\n";
        return 2;
    }

    int free_edges = (n - 1) * (n - 2) / 2;
    uint64_t total = uint64_t{1} << free_edges;
    if (limit && limit < total) total = limit;

    Checker checker(n);
    for (uint64_t bits = 0; bits < total; ++bits) {
        uint64_t graph_mask = even_graph_mask(n, bits);
        checker.compute_valid_subsets(graph_mask);
        if (!checker.has_partition()) {
            std::cout << "n=" << n << "\n";
            std::cout << "checked_before_counterexample=" << bits << "\n";
            std::cout << "counterexample_mask=" << graph_mask << "\n";
            return 0;
        }
        if (progress && bits && bits % 262144 == 0) {
            std::cerr << "checked=" << bits << "/" << total << "\n";
        }
    }
    std::cout << "n=" << n << "\n";
    std::cout << "checked=" << total << "\n";
    std::cout << "no_counterexample_seen\n";
    return 0;
}
