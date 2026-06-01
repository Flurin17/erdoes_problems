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
#include <unordered_set>
#include <vector>

namespace {

enum class RootMode {
    None,
    Edge,
    Nonedge,
    TriangleNonedge,
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
        adjacency.fill(0);
        int edge = 0;
        for (int u = 0; u < n; ++u) {
            for (int v = u + 1; v < n; ++v) {
                if ((graph_mask >> edge) & 1) {
                    adjacency[u] |= 1 << v;
                    adjacency[v] |= 1 << u;
                }
                ++edge;
            }
        }
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
        if (root_mode == RootMode::TriangleNonedge) {
            return has_triangle_partition(root_pair);
        }
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
    std::array<int, 10> adjacency{};
    std::unordered_set<uint64_t> triangle_failed;

    bool has_triangle_partition(std::optional<std::pair<int, int>> root_pair) {
        if (!root_pair) return false;
        triangle_failed.clear();
        return rec_triangle(
            full,
            0b1111,
            4,
            4,
            true,
            true,
            true,
            true,
            *root_pair
        );
    }

    static bool is_zero_slot(int slot) {
        return slot == 0 || slot == 1;
    }

    static uint64_t triangle_key(
        int remaining,
        int slot_mask,
        int first_slot,
        int second_slot,
        bool first_zero_clean,
        bool second_zero_clean,
        bool first_c_clean,
        bool second_c_clean
    ) {
        uint64_t key = static_cast<uint64_t>(remaining);
        key = (key << 4) | static_cast<uint64_t>(slot_mask);
        key = (key << 3) | static_cast<uint64_t>(first_slot);
        key = (key << 3) | static_cast<uint64_t>(second_slot);
        key = (key << 1) | static_cast<uint64_t>(first_zero_clean);
        key = (key << 1) | static_cast<uint64_t>(second_zero_clean);
        key = (key << 1) | static_cast<uint64_t>(first_c_clean);
        key = (key << 1) | static_cast<uint64_t>(second_c_clean);
        return key;
    }

    bool rec_triangle(
        int remaining,
        int slot_mask,
        int first_slot,
        int second_slot,
        bool first_zero_clean,
        bool second_zero_clean,
        bool first_c_clean,
        bool second_c_clean,
        std::pair<int, int> root_pair
    ) {
        if (remaining == 0) {
            bool direct =
                first_slot != second_slot
                && !(is_zero_slot(first_slot) && is_zero_slot(second_slot));
            bool zero_split =
                is_zero_slot(first_slot)
                && is_zero_slot(second_slot)
                && first_slot != second_slot;
            bool repair =
                zero_split
                && (
                    (first_zero_clean && first_c_clean)
                    || (second_zero_clean && second_c_clean)
                );
            return direct || repair;
        }
        if (slot_mask == 0) return false;
        uint64_t key = triangle_key(
            remaining,
            slot_mask,
            first_slot,
            second_slot,
            first_zero_clean,
            second_zero_clean,
            first_c_clean,
            second_c_clean
        );
        if (triangle_failed.find(key) != triangle_failed.end()) return false;

        constexpr std::array<int, 4> slot_residue{0, 0, 1, 2};
        for (int slot = 0; slot < 4; ++slot) {
            if (!((slot_mask >> slot) & 1)) continue;
            int next_slot_mask = slot_mask & ~(1 << slot);
            int target_residue = slot_residue[slot];
            for (int sub : submasks_with_pivot[remaining]) {
                if (residue[sub] != target_residue) continue;
                if (target_residue == 1 && !exact_matching[sub]) continue;

                int next_first_slot = first_slot;
                int next_second_slot = second_slot;
                bool next_first_zero_clean = first_zero_clean;
                bool next_second_zero_clean = second_zero_clean;
                bool next_first_c_clean = first_c_clean;
                bool next_second_c_clean = second_c_clean;

                if (slot == 2) {
                    next_first_c_clean =
                        __builtin_popcount(static_cast<unsigned>(
                            adjacency[root_pair.first] & sub
                        )) == 0;
                    next_second_c_clean =
                        __builtin_popcount(static_cast<unsigned>(
                            adjacency[root_pair.second] & sub
                        )) == 0;
                }
                if ((sub >> root_pair.first) & 1) {
                    next_first_slot = slot;
                    if (is_zero_slot(slot)) {
                        next_first_zero_clean =
                            __builtin_popcount(static_cast<unsigned>(
                                adjacency[root_pair.first] & sub
                            )) == 0;
                    }
                }
                if ((sub >> root_pair.second) & 1) {
                    next_second_slot = slot;
                    if (is_zero_slot(slot)) {
                        next_second_zero_clean =
                            __builtin_popcount(static_cast<unsigned>(
                                adjacency[root_pair.second] & sub
                            )) == 0;
                    }
                }

                if (rec_triangle(
                        remaining ^ sub,
                        next_slot_mask,
                        next_first_slot,
                        next_second_slot,
                        next_first_zero_clean,
                        next_second_zero_clean,
                        next_first_c_clean,
                        next_second_c_clean,
                        root_pair
                    )) {
                    return true;
                }
            }
        }
        triangle_failed.insert(key);
        return false;
    }

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

bool degree_bounds_ok(
    int n,
    uint64_t graph_mask,
    int min_degree,
    int max_degree,
    bool require_mixed_degree_residue
) {
    if (
        min_degree <= 0
        && max_degree >= n - 1
        && !require_mixed_degree_residue
    ) {
        return true;
    }
    std::array<int, 10> degrees{};
    int edge = 0;
    for (int u = 0; u < n; ++u) {
        for (int v = u + 1; v < n; ++v) {
            if ((graph_mask >> edge) & 1) {
                ++degrees[u];
                ++degrees[v];
            }
            ++edge;
        }
    }
    bool has_zero_residue = false;
    bool has_two_residue = false;
    for (int v = 0; v < n; ++v) {
        if (degrees[v] < min_degree || degrees[v] > max_degree) return false;
        int residue = degrees[v] % 4;
        if (residue == 0) has_zero_residue = true;
        if (residue == 2) has_two_residue = true;
    }
    return !require_mixed_degree_residue || (has_zero_residue && has_two_residue);
}

}  // namespace

int main(int argc, char** argv) {
    int n = 8;
    uint64_t start = 0;
    uint64_t limit = 0;
    uint64_t progress_every = 262144;
    bool progress = false;
    int min_degree = 0;
    int max_degree = -1;
    bool require_mixed_degree_residue = false;
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
        } else if (arg == "--min-degree" && i + 1 < argc) {
            min_degree = std::stoi(argv[++i]);
        } else if (arg == "--max-degree" && i + 1 < argc) {
            max_degree = std::stoi(argv[++i]);
        } else if (arg == "--mixed-degree-residue") {
            require_mixed_degree_residue = true;
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
        } else if (arg == "--triangle-nonedge" && i + 1 < argc) {
            if (root_mode != RootMode::None) {
                std::cerr << "only one rooted endpoint option is allowed\n";
                return 2;
            }
            std::string text = argv[++i];
            size_t sep = text.find(':');
            if (sep == std::string::npos) {
                std::cerr << "--triangle-nonedge expects u:v\n";
                return 2;
            }
            root_mode = RootMode::TriangleNonedge;
            root_pair = {
                std::stoi(text.substr(0, sep)),
                std::stoi(text.substr(sep + 1)),
            };
        } else if (arg == "--progress") {
            progress = true;
        } else {
            std::cerr << "usage: matching_slot_fast [--n N] [--start S]"
                      << " [--limit L] [--good-edge u:v]"
                      << " [--good-nonedge u:v]"
                      << " [--triangle-nonedge u:v] [--progress]"
                      << " [--progress-every P]"
                      << " [--min-degree D] [--max-degree D]"
                      << " [--mixed-degree-residue]\n";
            return 2;
        }
    }
    if (n < 1 || n > 10) {
        std::cerr << "supported range: 1 <= n <= 10\n";
        return 2;
    }
    if (max_degree < 0) max_degree = n - 1;
    if (min_degree < 0 || max_degree > n - 1 || min_degree > max_degree) {
        std::cerr << "invalid degree bounds\n";
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
            if (
                (root_mode == RootMode::Nonedge
                 || root_mode == RootMode::TriangleNonedge)
                && present
            ) {
                continue;
            }
        }
        if (!degree_bounds_ok(
                n,
                graph_mask,
                min_degree,
                max_degree,
                require_mixed_degree_residue
            )) {
            continue;
        }
        ++checked;
        checker.compute_valid_subsets(graph_mask);
        if (!checker.has_partition(root_mode, root_pair)) {
            std::cout << "n=" << n << "\n";
            if (root_pair) {
                if (root_mode == RootMode::Edge) std::cout << "good_edge=";
                else if (root_mode == RootMode::Nonedge) std::cout << "good_nonedge=";
                else std::cout << "triangle_nonedge=";
                std::cout << root_pair->first << ":" << root_pair->second << "\n";
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
        if (root_mode == RootMode::Edge) std::cout << "good_edge=";
        else if (root_mode == RootMode::Nonedge) std::cout << "good_nonedge=";
        else std::cout << "triangle_nonedge=";
        std::cout << root_pair->first << ":" << root_pair->second << "\n";
    }
    std::cout << "bit_start=" << start << "\n";
    std::cout << "bit_stop=" << stop << "\n";
    if (min_degree != 0) std::cout << "min_degree=" << min_degree << "\n";
    if (max_degree != n - 1) std::cout << "max_degree=" << max_degree << "\n";
    if (require_mixed_degree_residue) std::cout << "mixed_degree_residue=True\n";
    std::cout << "checked=" << checked << "\n";
    std::cout << "no_counterexample_seen\n";
    return 0;
}
