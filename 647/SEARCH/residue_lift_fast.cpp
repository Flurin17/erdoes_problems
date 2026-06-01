#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using u64 = uint64_t;
using u128 = __uint128_t;

static constexpr int BASE_RESIDUES[] = {
    0, 858, 1287, 1716, 2431, 2574, 4862, 5291, 6149, 8151,
    9009, 9867, 10582, 12155, 12584, 13013, 13442, 16302,
    17017, 17160, 18733, 19877, 20306, 20735, 21164, 24310,
    24453, 25168, 27170, 28028, 28457, 29315, 29601, 31603,
    32032, 32461, 35321, 36608, 37752, 38896, 44187,
};

static constexpr int BASE_PRIMES[] = {11, 13, 17, 19};
static constexpr int SMALL_PRIMES[] = {2, 3, 5, 7};
static constexpr int SMALL_EXPONENT_CAPS[] = {3, 2, 1, 1};

[[noreturn]] static void die(const std::string& msg) {
    std::cerr << msg << "\n";
    std::exit(2);
}

static std::vector<int> parse_primes(const std::string& text) {
    std::vector<int> primes;
    if (text.empty()) return primes;
    std::stringstream ss(text);
    std::string part;
    while (std::getline(ss, part, ',')) {
        if (!part.empty()) primes.push_back(std::stoi(part));
    }
    return primes;
}

static u64 encode_key(const std::vector<int>& exponents, int bound) {
    u64 code = 0;
    for (int exponent : exponents) {
        code = code * 5 + (u64)exponent;
    }
    return (code << 16) | (u64)bound;
}

struct SmoothCache {
    std::vector<int> primes;
    std::unordered_map<u64, u64> cache;

    u64 max_forced_smooth(const std::vector<int>& exponents, int bound) {
        u64 key = encode_key(exponents, bound);
        auto found = cache.find(key);
        if (found != cache.end()) return found->second;

        std::vector<size_t> indexes;
        indexes.reserve(exponents.size());
        u64 forced = 1;
        int divisors = 1;
        for (size_t i = 0; i < exponents.size(); ++i) {
            if (exponents[i] == 0) continue;
            indexes.push_back(i);
            for (int j = 0; j < exponents[i]; ++j) forced *= (u64)primes[i];
            divisors *= exponents[i] + 1;
        }
        if (indexes.empty()) {
            cache.emplace(key, 1);
            return 1;
        }

        u64 best = 0;
        auto dfs = [&](auto&& self, size_t pos, u64 value, int tau_value) -> void {
            if (pos == indexes.size()) {
                if (value > best) best = value;
                return;
            }

            size_t index = indexes[pos];
            u64 prime = (u64)primes[index];
            int base_exponent = exponents[index];
            u64 current = value;
            for (int exponent = base_exponent;; ++exponent) {
                int next_tau = tau_value / (base_exponent + 1) * (exponent + 1);
                if (next_tau > bound) break;
                self(self, pos + 1, current, next_tau);
                if (current > UINT64_MAX / prime) break;
                current *= prime;
            }
        };

        dfs(dfs, 0, forced, divisors);
        cache.emplace(key, best);
        return best;
    }
};

static bool residue_ok(u64 residue, u64 modulus, int k_limit,
                       const std::vector<int>& primes,
                       const std::vector<int>& exponent_caps,
                       SmoothCache& smooth_cache) {
    u64 q_modulus = 2520ULL * modulus;
    for (int k = 1; k <= k_limit; ++k) {
        u64 value = (u64)(((u128)2520 * residue + q_modulus - (u64)k) % q_modulus);
        if (value == 0) value = q_modulus;

        int forced_tau = 1;
        std::vector<int> exponents;
        exponents.reserve(primes.size());
        u64 remaining = value;
        for (size_t i = 0; i < primes.size(); ++i) {
            int exponent = 0;
            while (exponent < exponent_caps[i] && remaining % (u64)primes[i] == 0) {
                remaining /= (u64)primes[i];
                ++exponent;
            }
            exponents.push_back(exponent);
            forced_tau *= exponent + 1;
        }

        int bound = k + 2;
        if (forced_tau > bound) return false;
        if (2 * forced_tau > bound) {
            u64 smooth_limit = smooth_cache.max_forced_smooth(exponents, bound);
            if (value > smooth_limit) return false;
        }
    }
    return true;
}

struct Args {
    int k_limit = 200;
    std::vector<int> add_primes = {23};
    std::string format = "lines";
};

static Args parse_args(int argc, char** argv) {
    Args args;
    for (int i = 1; i < argc; ++i) {
        std::string key = argv[i];
        auto need = [&]() -> std::string {
            if (++i >= argc) die("missing value for " + key);
            return argv[i];
        };
        if (key == "--k") args.k_limit = std::stoi(need());
        else if (key == "--add-primes") args.add_primes = parse_primes(need());
        else if (key == "--format") args.format = need();
        else die("unknown arg " + key);
    }
    if (args.k_limit <= 0) die("--k must be positive");
    if (args.format != "lines" && args.format != "csv") die("--format must be lines or csv");
    return args;
}

int main(int argc, char** argv) {
    Args args = parse_args(argc, argv);

    u64 modulus = 1;
    for (int prime : BASE_PRIMES) modulus *= (u64)prime;
    std::vector<u64> residues(std::begin(BASE_RESIDUES), std::end(BASE_RESIDUES));
    std::vector<int> current_extra(std::begin(BASE_PRIMES), std::end(BASE_PRIMES));

    for (int prime : args.add_primes) {
        u64 new_modulus = modulus * (u64)prime;
        current_extra.push_back(prime);

        std::vector<int> primes(std::begin(SMALL_PRIMES), std::end(SMALL_PRIMES));
        primes.insert(primes.end(), current_extra.begin(), current_extra.end());
        std::vector<int> exponent_caps(std::begin(SMALL_EXPONENT_CAPS), std::end(SMALL_EXPONENT_CAPS));
        exponent_caps.resize(primes.size(), 1);
        SmoothCache smooth_cache{primes, {}};

        std::vector<u64> lifted;
        lifted.reserve(residues.size() * (size_t)prime);
        for (u64 residue : residues) {
            for (int digit = 0; digit < prime; ++digit) {
                u64 candidate = residue + modulus * (u64)digit;
                if (residue_ok(candidate, new_modulus, args.k_limit, primes, exponent_caps, smooth_cache)) {
                    lifted.push_back(candidate);
                }
            }
        }

        modulus = new_modulus;
        residues.swap(lifted);
        std::cout << "LIFT prime=" << prime
                  << " modulus=" << modulus
                  << " count=" << residues.size()
                  << " density=" << (double)residues.size() / (double)modulus
                  << "\n";
    }

    std::cout << "RESULT modulus=" << modulus << " count=" << residues.size() << "\n";
    if (args.format == "csv") {
        for (size_t i = 0; i < residues.size(); ++i) {
            if (i) std::cout << ",";
            std::cout << residues[i];
        }
        std::cout << "\n";
    } else {
        for (u64 residue : residues) std::cout << residue << "\n";
    }
    return 0;
}
