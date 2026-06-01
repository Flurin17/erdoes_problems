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
#include <optional>
#include <string>
#include <vector>

namespace {

enum class RootMode {
    None,
    Edge,
    Nonedge,
};

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
          submasks_with_pivot(1 << n_value),
          memo(1 << n_value) {
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

    bool has_partition(
        RootMode root_mode,
        std::optional<std::pair<int, int>> root_pair
    ) {
        for (auto& table : memo) {
            for (auto& row : table) row.fill(-1);
        }
        std::array<int, 4> counts{2, 1, 1, 0};
        return rec(full, state_code(counts), 4, 4, root_mode, root_pair);
    }

  private:
    int n;
    int full;
    std::vector<std::array<uint64_t, 10>> incident;
    std::vector<std::vector<int>> submasks_with_pivot;
    std::array<int, 1 << 10> residue{};
    std::array<bool, 1 << 10> exact_matching{};
    std::vector<std::array<std::array<int8_t, 25>, 625>> memo;

    bool rec(
        int remaining,
        int code,
        int first_residue,
        int second_residue,
        RootMode root_mode,
        std::optional<std::pair<int, int>> root_pair
    ) {
        if (remaining == 0) {
            if (root_mode == RootMode::None) return true;
            bool different_nonzero_split =
                first_residue != second_residue
                && !(first_residue < 2 && second_residue < 2);
            if (root_mode == RootMode::Nonedge) return different_nonzero_split;
            return (first_residue == 2 && second_residue == 2)
                || different_nonzero_split;
        }
        if (code == 0) return false;
        int endpoint_code = first_residue * 5 + second_residue;
        int8_t& saved = memo[remaining][code][endpoint_code];
        if (saved != -1) return saved;
        for (int r = 0; r < 3; ++r) {
            if (!has_count(code, r)) continue;
            int next_code = remove_count(code, r);
            for (int sub : submasks_with_pivot[remaining]) {
                if (residue[sub] != r) continue;
                if (r == 1 && !exact_matching[sub]) continue;
                int next_first = first_residue;
                int next_second = second_residue;
                if (root_pair) {
                    if ((sub >> root_pair->first) & 1) next_first = r;
                    if ((sub >> root_pair->second) & 1) next_second = r;
                }
                if (rec(
                        remaining ^ sub,
                        next_code,
                        next_first,
                        next_second,
                        root_mode,
                        root_pair
                    )) {
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
    uint64_t start = 0;
    uint64_t limit = 0;
    uint64_t progress_every = 262144;
    bool progress = false;
    RootMode root_mode = RootMode::None;
    std::optional<std::pair<int, int>> root_pair;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--n" && i + 1 < argc) {
            n = std::stoi(argv[++i]);
        } else if (arg == "--start" && i + 1 < argc) {
            start = std::stoull(argv[++i]);
        } else if (arg == "--limit" && i + 1 < argc) {
            limit = std::stoull(argv[++i]);
        } else if (arg == "--progress-every" && i + 1 < argc) {
            progress_every = std::stoull(argv[++i]);
        } else if (arg == "--good-edge" && i + 1 < argc) {
            if (root_mode != RootMode::None) {
                std::cerr << "only one rooted endpoint option is allowed\n";
                return 2;
            }
            std::string text = argv[++i];
            size_t sep = text.find(':');
            if (sep == std::string::npos) {
                std::cerr << "--good-edge expects u:v\n";
                return 2;
            }
            root_mode = RootMode::Edge;
            root_pair = {
                std::stoi(text.substr(0, sep)),
                std::stoi(text.substr(sep + 1)),
            };
        } else if (arg == "--good-nonedge" && i + 1 < argc) {
            if (root_mode != RootMode::None) {
                std::cerr << "only one rooted endpoint option is allowed\n";
                return 2;
            }
            std::string text = argv[++i];
            size_t sep = text.find(':');
            if (sep == std::string::npos) {
                std::cerr << "--good-nonedge expects u:v\n";
                return 2;
            }
            root_mode = RootMode::Nonedge;
            root_pair = {
                std::stoi(text.substr(0, sep)),
                std::stoi(text.substr(sep + 1)),
            };
        } else if (arg == "--progress") {
            progress = true;
        } else {
            std::cerr << "usage: matching_slot_fast [--n N] [--start S]"
                      << " [--limit L] [--good-edge u:v]"
                      << " [--good-nonedge u:v] [--progress]"
                      << " [--progress-every P]\n";
            return 2;
        }
    }
    if (n < 1 || n > 10) {
        std::cerr << "supported range: 1 <= n <= 10\n";
        return 2;
    }
    if (root_pair) {
        if (
            root_pair->first < 0 || root_pair->first >= n
            || root_pair->second < 0 || root_pair->second >= n
            || root_pair->first == root_pair->second
        ) {
            std::cerr << "rooted endpoints must be distinct vertices in range\n";
            return 2;
        }
        if (root_pair->first > root_pair->second) {
            std::swap(root_pair->first, root_pair->second);
        }
    }

    int free_edges = (n - 1) * (n - 2) / 2;
    uint64_t all_bits = uint64_t{1} << free_edges;
    uint64_t stop = all_bits;
    if (limit && limit < stop) stop = limit;
    if (start > stop) {
        std::cerr << "--start must be at most the exclusive stop bound\n";
        return 2;
    }

    Checker checker(n);
    uint64_t checked = 0;
    for (uint64_t bits = start; bits < stop; ++bits) {
        uint64_t graph_mask = even_graph_mask(n, bits);
        if (root_pair) {
            int idx = edge_index(n, root_pair->first, root_pair->second);
            bool present = ((graph_mask >> idx) & 1) != 0;
            if (root_mode == RootMode::Edge && !present) continue;
            if (root_mode == RootMode::Nonedge && present) continue;
        }
        ++checked;
        checker.compute_valid_subsets(graph_mask);
        if (!checker.has_partition(root_mode, root_pair)) {
            std::cout << "n=" << n << "\n";
            if (root_pair) {
                std::cout
                    << (root_mode == RootMode::Edge ? "good_edge=" : "good_nonedge=")
                    << root_pair->first << ":" << root_pair->second << "\n";
            }
            std::cout << "checked_before_counterexample=" << checked << "\n";
            std::cout << "counterexample_mask=" << graph_mask << "\n";
            return 0;
        }
        if (
            progress
            && progress_every
            && bits > start
            && (bits - start) % progress_every == 0
        ) {
            std::cerr << "bits=" << bits << "/" << stop
                      << " checked=" << checked << "\n";
        }
    }
    std::cout << "n=" << n << "\n";
    if (root_pair) {
        std::cout
            << (root_mode == RootMode::Edge ? "good_edge=" : "good_nonedge=")
            << root_pair->first << ":" << root_pair->second << "\n";
    }
    std::cout << "bit_start=" << start << "\n";
    std::cout << "bit_stop=" << stop << "\n";
    std::cout << "checked=" << checked << "\n";
    std::cout << "no_counterexample_seen\n";
    return 0;
}
