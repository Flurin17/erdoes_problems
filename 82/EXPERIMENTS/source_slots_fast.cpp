// Exact source-residue fixed-slot checks for small dyadic lifts.
//
// For the lift q -> M, this enumerates labelled graphs whose full vertex set
// has one common degree residue modulo q, then tests fixed M-modular slot
// multisets.  The exhaustive mode chooses all edges among the first n-1
// vertices and solves the incident edges to the last vertex.  For q=4 this
// reduces the n=8 search from 2^28 full masks to 2^21 internal masks.  The
// random-sample mode uses the same solved-edge representation for deterministic
// seeded probes at n=10 and n=11.

#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

using Candidate = std::vector<int>;

namespace {

int positive_mod(int value, int modulus) {
    value %= modulus;
    if (value < 0) value += modulus;
    return value;
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

std::vector<Candidate> all_candidates(int modulus, int slot_count) {
    std::vector<Candidate> out;
    Candidate current;
    auto rec = [&](auto&& self, int start, int remaining) -> void {
        if (remaining == 0) {
            out.push_back(current);
            return;
        }
        for (int value = start; value < modulus; ++value) {
            current.push_back(value);
            self(self, value, remaining - 1);
            current.pop_back();
        }
    };
    rec(rec, 0, slot_count);
    return out;
}

std::vector<Candidate> parse_candidates(
    const std::string& text,
    int modulus,
    int slot_count
) {
    if (text.empty()) return all_candidates(modulus, slot_count);
    std::vector<Candidate> out;
    std::stringstream blocks(text);
    std::string block;
    while (std::getline(blocks, block, ';')) {
        if (block.empty()) continue;
        std::stringstream items(block);
        std::string item;
        Candidate cand;
        while (std::getline(items, item, ',')) {
            if (item.empty()) continue;
            cand.push_back(positive_mod(std::stoi(item), modulus));
        }
        if (cand.empty()) {
            std::cerr << "candidate must have at least one slot: " << block << "\n";
            std::exit(2);
        }
        std::sort(cand.begin(), cand.end());
        out.push_back(cand);
    }
    return out;
}

std::string candidate_string(const Candidate& cand) {
    std::ostringstream out;
    for (size_t i = 0; i < cand.size(); ++i) {
        if (i) out << ",";
        out << cand[i];
    }
    return out.str();
}

uint64_t state_code(const Candidate& cand, int modulus, int base) {
    uint64_t place = 1;
    uint64_t code = 0;
    for (int residue = 0; residue < modulus; ++residue) {
        int count = 0;
        for (int slot : cand) {
            if (slot == residue) ++count;
        }
        code += count * place;
        place *= base;
    }
    return code;
}

bool has_count(uint64_t code, int residue, int base) {
    for (int i = 0; i < residue; ++i) code /= base;
    return code % base;
}

uint64_t remove_count(uint64_t code, int residue, int base) {
    uint64_t place = 1;
    for (int i = 0; i < residue; ++i) place *= base;
    return code - place;
}

class Checker {
  public:
    Checker(int n_value, int target_modulus_value)
        : n(n_value),
          target_modulus(target_modulus_value),
          full((1 << n_value) - 1),
          incident(1 << n_value),
          submasks_with_pivot(1 << n_value),
          residue(1 << n_value, -1) {
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

    void compute_residues(uint64_t graph_mask) {
        std::fill(residue.begin(), residue.end(), -1);
        for (int subset = 1; subset <= full; ++subset) {
            int first = __builtin_ctz(static_cast<unsigned>(subset));
            int value =
                __builtin_popcountll(graph_mask & incident[subset][first])
                % target_modulus;
            bool ok = true;
            int rest = subset & ~(1 << first);
            while (rest) {
                int bit = rest & -rest;
                int v = __builtin_ctz(static_cast<unsigned>(bit));
                int here =
                    __builtin_popcountll(graph_mask & incident[subset][v])
                    % target_modulus;
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
        failed.clear();
        int base = static_cast<int>(cand.size()) + 1;
        return rec(full, state_code(cand, target_modulus, base), base);
    }

  private:
    int n;
    int target_modulus;
    int full;
    std::vector<std::array<uint64_t, 12>> incident;
    std::vector<std::vector<int>> submasks_with_pivot;
    std::vector<int> residue;
    std::unordered_set<uint64_t> failed;

    bool rec(int remaining, uint64_t code, int base) {
        if (remaining == 0) return true;
        if (code == 0) return false;
        uint64_t key = (static_cast<uint64_t>(remaining) << 48) | code;
        if (failed.find(key) != failed.end()) return false;
        int pivot = remaining & -remaining;
        int pivot_index = __builtin_ctz(static_cast<unsigned>(pivot));
        for (int r = 0; r < target_modulus; ++r) {
            if (!has_count(code, r, base)) continue;
            uint64_t next_code = remove_count(code, r, base);
            for (int sub : submasks_with_pivot[remaining]) {
                if (!((sub >> pivot_index) & 1)) continue;
                if (residue[sub] != r) continue;
                if (rec(remaining ^ sub, next_code, base)) return true;
            }
        }
        failed.insert(key);
        return false;
    }
};

uint64_t source_modular_mask(
    int n,
    uint64_t bits,
    int source_modulus,
    int source_residue,
    bool& ok
) {
    ok = false;
    uint64_t graph_mask = 0;
    std::array<int, 12> degrees{};
    int bit_index = 0;
    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n - 1; ++j) {
            if ((bits >> bit_index) & 1) {
                int idx = edge_index(n, i, j);
                graph_mask |= uint64_t{1} << idx;
                ++degrees[i];
                ++degrees[j];
            }
            ++bit_index;
        }
    }

    for (int i = 0; i < n - 1; ++i) {
        int diff = positive_mod(source_residue - degrees[i], source_modulus);
        if (diff > 1) return 0;
        if (diff == 1) {
            int idx = edge_index(n, i, n - 1);
            graph_mask |= uint64_t{1} << idx;
            ++degrees[i];
            ++degrees[n - 1];
        }
    }
    if (degrees[n - 1] % source_modulus != source_residue) return 0;
    ok = true;
    return graph_mask;
}

}  // namespace

int main(int argc, char** argv) {
    int n = 8;
    int source_modulus = 4;
    int target_modulus = 8;
    int source_residue = -1;
    int slot_count = 4;
    uint64_t start = 0;
    uint64_t limit = 0;
    uint64_t random_samples = 0;
    uint64_t seed = 1;
    bool progress = false;
    bool quiet_kills = false;
    uint64_t progress_every = 262144;
    std::string candidate_text;

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "--n" && i + 1 < argc) {
            n = std::stoi(argv[++i]);
        } else if (arg == "--source-modulus" && i + 1 < argc) {
            source_modulus = std::stoi(argv[++i]);
        } else if (arg == "--target-modulus" && i + 1 < argc) {
            target_modulus = std::stoi(argv[++i]);
        } else if (arg == "--source-residue" && i + 1 < argc) {
            source_residue = std::stoi(argv[++i]);
        } else if (arg == "--slot-count" && i + 1 < argc) {
            slot_count = std::stoi(argv[++i]);
        } else if (arg == "--candidates" && i + 1 < argc) {
            candidate_text = argv[++i];
        } else if (arg == "--start" && i + 1 < argc) {
            start = std::stoull(argv[++i]);
        } else if (arg == "--limit" && i + 1 < argc) {
            limit = std::stoull(argv[++i]);
        } else if (arg == "--random-samples" && i + 1 < argc) {
            random_samples = std::stoull(argv[++i]);
        } else if (arg == "--seed" && i + 1 < argc) {
            seed = std::stoull(argv[++i]);
        } else if (arg == "--progress") {
            progress = true;
        } else if (arg == "--quiet-kills") {
            quiet_kills = true;
        } else if (arg == "--progress-every" && i + 1 < argc) {
            progress_every = std::stoull(argv[++i]);
        } else {
            std::cerr << "usage: source_slots_fast [--n N]"
                      << " [--source-modulus q] [--target-modulus M]"
                      << " [--source-residue a]"
                      << " [--candidates r,...;...] [--slot-count B]"
                      << " [--start S] [--limit L]"
                      << " [--random-samples N] [--seed S]"
                      << " [--progress] [--quiet-kills]\n";
            return 2;
        }
    }

    if (n < 1 || n > 11) {
        std::cerr << "supported range: 1 <= n <= 11\n";
        return 2;
    }
    if (source_modulus <= 0 || target_modulus <= 0 || slot_count <= 0) {
        std::cerr << "invalid modulus or slot count\n";
        return 2;
    }
    if (target_modulus > 16 || slot_count > 5) {
        std::cerr << "target modulus and slot count are intentionally capped\n";
        return 2;
    }
    if (source_residue >= 0) {
        source_residue = positive_mod(source_residue, source_modulus);
    }

    int free_edges = (n - 1) * (n - 2) / 2;
    uint64_t all_bits = uint64_t{1} << free_edges;
    uint64_t stop = all_bits;
    if (limit && limit < stop) stop = limit;
    if (start > stop) {
        std::cerr << "--start must be at most the exclusive stop bound\n";
        return 2;
    }

    std::vector<Candidate> candidates =
        parse_candidates(candidate_text, target_modulus, slot_count);
    std::vector<int> alive(candidates.size(), 1);
    std::vector<uint64_t> bad(candidates.size(), 0);
    std::vector<uint64_t> killed_at_checked(candidates.size(), 0);
    Checker checker(n, target_modulus);

    uint64_t checked = 0;
    uint64_t attempted = 0;
    auto process_bits = [&](uint64_t bits) {
        for (int a = 0; a < source_modulus; ++a) {
            if (source_residue >= 0 && a != source_residue) continue;
            bool ok = false;
            uint64_t graph_mask = source_modular_mask(n, bits, source_modulus, a, ok);
            if (!ok) continue;
            ++checked;
            checker.compute_residues(graph_mask);
            for (size_t i = 0; i < candidates.size(); ++i) {
                if (!alive[i]) continue;
                if (!checker.has_partition(candidates[i])) {
                    alive[i] = 0;
                    bad[i] = graph_mask;
                    killed_at_checked[i] = checked;
                    if (!quiet_kills) {
                        std::cout << "killed=" << candidate_string(candidates[i])
                                  << " source_residue=" << a
                                  << " mask=" << graph_mask
                                  << " checked=" << checked
                                  << " internal_bits=" << bits << "\n";
                    }
                }
            }
        }
    };

    if (random_samples) {
        std::mt19937_64 rng(seed);
        for (uint64_t sample = 0; sample < random_samples; ++sample) {
            uint64_t bits = rng() & (all_bits - 1);
            ++attempted;
            process_bits(bits);
            if (progress && progress_every && sample > 0 && sample % progress_every == 0) {
                std::cerr << "samples=" << sample << "/" << random_samples
                          << " source_modular_checked=" << checked << "\n";
            }
        }
    } else {
        for (uint64_t bits = start; bits < stop; ++bits) {
            ++attempted;
            process_bits(bits);
            if (progress && progress_every && bits > start && (bits - start) % progress_every == 0) {
                std::cerr << "bits=" << bits << "/" << stop
                          << " source_modular_checked=" << checked << "\n";
            }
        }
    }

    int good_count = 0;
    std::cout << "n=" << n << "\n";
    std::cout << "source_modulus=" << source_modulus << "\n";
    std::cout << "target_modulus=" << target_modulus << "\n";
    if (source_residue >= 0) std::cout << "source_residue=" << source_residue << "\n";
    std::cout << "bit_start=" << start << "\n";
    std::cout << "bit_stop=" << stop << "\n";
    if (random_samples) {
        std::cout << "random_samples=" << random_samples << "\n";
        std::cout << "seed=" << seed << "\n";
    }
    std::cout << "attempted=" << attempted << "\n";
    std::cout << "source_modular_checked=" << checked << "\n";
    for (size_t i = 0; i < candidates.size(); ++i) {
        std::cout << "slots=" << candidate_string(candidates[i]) << " ";
        if (alive[i]) {
            std::cout << "ok\n";
            ++good_count;
        } else {
            std::cout << "bad=" << bad[i]
                      << " checked=" << killed_at_checked[i] << "\n";
        }
    }
    std::cout << "good_count=" << good_count << "\n";
    for (size_t i = 0; i < candidates.size(); ++i) {
        if (alive[i]) std::cout << "good=" << candidate_string(candidates[i]) << "\n";
    }
    return 0;
}
