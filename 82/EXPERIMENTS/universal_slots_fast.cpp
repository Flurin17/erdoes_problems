// Exact fixed-slot checks for small fixed-parity graphs.
//
// This is a C++ version of universal_slots.py for the exhaustive n=8 range.
// It enumerates labelled graphs whose degrees all have a prescribed parity by
// choosing all edges not incident with the last vertex and then adding the
// unique parity-correction edges to the last vertex.  For each graph it checks
// whether each residue-slot multiset admits an exact cover by induced
// 4-modular parts using those slots.

#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>

using Candidate = std::array<int, 4>;

namespace {

std::vector<std::pair<int, int>> edge_order(int n) {
    std::vector<std::pair<int, int>> edges;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) edges.push_back({i, j});
    }
    return edges;
}

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

std::vector<Candidate> all_candidates(int modulus) {
    std::vector<Candidate> out;
    for (int a = 0; a < modulus; ++a) {
        for (int b = a; b < modulus; ++b) {
            for (int c = b; c < modulus; ++c) {
                for (int d = c; d < modulus; ++d) out.push_back({a, b, c, d});
            }
        }
    }
    return out;
}

std::vector<Candidate> parse_candidates(const std::string& text, int modulus) {
    if (text.empty()) return all_candidates(modulus);
    std::vector<Candidate> out;
    std::stringstream blocks(text);
    std::string block;
    while (std::getline(blocks, block, ';')) {
        if (block.empty()) continue;
        std::stringstream items(block);
        std::string item;
        Candidate cand{0, 0, 0, 0};
        int idx = 0;
        while (std::getline(items, item, ',')) {
            if (item.empty()) continue;
            if (idx >= 4) {
                std::cerr << "candidate has more than four slots: " << block << "\n";
                std::exit(2);
            }
            cand[idx++] = std::stoi(item) % modulus;
        }
        if (idx != 4) {
            std::cerr << "candidate must have four slots: " << block << "\n";
            std::exit(2);
        }
        std::sort(cand.begin(), cand.end());
        out.push_back(cand);
    }
    return out;
}

std::string candidate_string(const Candidate& cand) {
    std::ostringstream out;
    for (int i = 0; i < 4; ++i) {
        if (i) out << ",";
        out << cand[i];
    }
    return out.str();
}

int state_code(const Candidate& cand) {
    int pow5 = 1;
    int code = 0;
    for (int r = 0; r < 4; ++r) {
        int count = 0;
        for (int slot : cand) {
            if (slot == r) ++count;
        }
        code += count * pow5;
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
    explicit Checker(int n_value, int modulus_value, bool odd_parts_value)
        : n(n_value),
          modulus(modulus_value),
          odd_parts(odd_parts_value),
          full((1 << n_value) - 1),
          incident(1 << n_value),
          submasks_with_pivot(1 << n_value) {
        auto edges = edge_order(n);
        for (int subset = 1; subset <= full; ++subset) {
            for (int v = 0; v < n; ++v) {
                if (!((subset >> v) & 1)) continue;
                uint64_t mask = 0;
                for (int w = 0; w < n; ++w) {
                    if (v == w || !((subset >> w) & 1)) continue;
                    int idx = edge_index(n, v, w);
                    mask |= (uint64_t{1} << idx);
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

    void compute_residues(uint64_t graph_mask) {
        residue.fill(-1);
        for (int subset = 1; subset <= full; ++subset) {
            int first = __builtin_ctz(static_cast<unsigned>(subset));
            int value = __builtin_popcountll(graph_mask & incident[subset][first]) % modulus;
            bool ok = true;
            int rest = subset & ~(1 << first);
            while (rest) {
                int bit = rest & -rest;
                int v = __builtin_ctz(static_cast<unsigned>(bit));
                int here = __builtin_popcountll(graph_mask & incident[subset][v]) % modulus;
                if (here != value) {
                    ok = false;
                    break;
                }
                rest ^= bit;
            }
            if (ok) residue[subset] = value;
        }
    }

    bool has_partition(const Candidate& cand) {
        for (auto& row : memo) row.fill(-1);
        return rec(full, state_code(cand));
    }

  private:
    int n;
    int modulus;
    bool odd_parts;
    int full;
    std::vector<std::array<uint64_t, 8>> incident;
    std::vector<std::vector<int>> submasks_with_pivot;
    std::array<int, 1 << 10> residue{};
    std::array<std::array<int8_t, 625>, 1 << 10> memo{};

    bool rec(int remaining, int code) {
        if (remaining == 0) return true;
        if (code == 0) return false;
        int8_t& saved = memo[remaining][code];
        if (saved != -1) return saved;
        for (int r = 0; r < modulus; ++r) {
            if (!has_count(code, r)) continue;
            int next_code = remove_count(code, r);
            for (int sub : submasks_with_pivot[remaining]) {
                if (odd_parts && (__builtin_popcount(static_cast<unsigned>(sub)) % 2 == 0)) {
                    continue;
                }
                if (residue[sub] == r && rec(remaining ^ sub, next_code)) {
                    saved = 1;
                    return true;
                }
            }
        }
        saved = 0;
        return false;
    }
};

uint64_t fixed_parity_graph_mask(int n, uint64_t bits, int degree_parity) {
    uint64_t graph_mask = 0;
    std::array<int, 10> parity{};
    int bit_index = 0;
    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n - 1; ++j) {
            if ((bits >> bit_index) & 1) {
                int idx = edge_index(n, i, j);
                graph_mask |= (uint64_t{1} << idx);
                parity[i] ^= 1;
                parity[j] ^= 1;
            }
            ++bit_index;
        }
    }
    for (int i = 0; i < n - 1; ++i) {
        if (parity[i] != degree_parity) {
            int idx = edge_index(n, i, n - 1);
            graph_mask |= (uint64_t{1} << idx);
            parity[n - 1] ^= 1;
        }
    }
    return graph_mask;
}

}  // namespace

int main(int argc, char** argv) {
    int n = 8;
    int modulus = 4;
    int degree_parity = 0;
    bool odd_parts = false;
    bool progress = false;
    std::string candidate_text;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--n" && i + 1 < argc) {
            n = std::stoi(argv[++i]);
        } else if (arg == "--modulus" && i + 1 < argc) {
            modulus = std::stoi(argv[++i]);
        } else if (arg == "--candidates" && i + 1 < argc) {
            candidate_text = argv[++i];
        } else if (arg == "--degree-parity" && i + 1 < argc) {
            degree_parity = std::stoi(argv[++i]) & 1;
        } else if (arg == "--odd-parts") {
            odd_parts = true;
        } else if (arg == "--progress") {
            progress = true;
        } else {
            std::cerr << "usage: universal_slots_fast [--n N] [--modulus 4]"
                      << " [--candidates a,b,c,d;...] [--degree-parity 0|1]"
                      << " [--odd-parts] [--progress]\n";
            return 2;
        }
    }
    if (n < 1 || n > 10 || modulus != 4) {
        std::cerr << "supported range: 1 <= n <= 10 and modulus 4\n";
        return 2;
    }
    if ((n * degree_parity) & 1) {
        std::cerr << "no graphs have all degrees congruent to " << degree_parity
                  << " mod 2 on " << n << " vertices\n";
        return 2;
    }

    std::vector<Candidate> candidates = parse_candidates(candidate_text, modulus);
    std::vector<int> alive(candidates.size(), 1);
    std::vector<uint64_t> bad(candidates.size(), 0);
    Checker checker(n, modulus, odd_parts);

    int free_edges = (n - 1) * (n - 2) / 2;
    uint64_t total = uint64_t{1} << free_edges;
    for (uint64_t bits = 0; bits < total; ++bits) {
        uint64_t graph_mask = fixed_parity_graph_mask(n, bits, degree_parity);
        checker.compute_residues(graph_mask);
        for (size_t i = 0; i < candidates.size(); ++i) {
            if (!alive[i]) continue;
            if (!checker.has_partition(candidates[i])) {
                alive[i] = 0;
                bad[i] = graph_mask;
                std::cout << "killed=" << candidate_string(candidates[i])
                          << " mask=" << graph_mask
                          << " graph_index=" << bits << "\n";
            }
        }
        if (progress && bits && bits % 262144 == 0) {
            std::cerr << "checked=" << bits << "/" << total << "\n";
        }
    }

    int good_count = 0;
    std::cout << "n=" << n << "\n";
    std::cout << "modulus=" << modulus << "\n";
    std::cout << "degree_parity=" << degree_parity << "\n";
    std::cout << "odd_parts=" << (odd_parts ? 1 : 0) << "\n";
    std::cout << "fixed_parity_graphs=" << total << "\n";
    for (size_t i = 0; i < candidates.size(); ++i) {
        std::cout << "slots=" << candidate_string(candidates[i]) << " "
                  << (alive[i] ? "ok" : ("bad=" + std::to_string(bad[i])))
                  << "\n";
        if (alive[i]) ++good_count;
    }
    std::cout << "good_count=" << good_count << "\n";
    for (size_t i = 0; i < candidates.size(); ++i) {
        if (alive[i]) std::cout << "good=" << candidate_string(candidates[i]) << "\n";
    }
    return 0;
}
