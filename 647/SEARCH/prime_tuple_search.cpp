#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <numeric>
#include <random>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

using u64 = uint64_t;
using u128 = __uint128_t;

static u64 mul_mod(u64 a, u64 b, u64 mod) {
    return static_cast<u64>((u128)a * b % mod);
}

static u64 pow_mod(u64 a, u64 e, u64 mod) {
    u64 r = 1;
    while (e) {
        if (e & 1) r = mul_mod(r, a, mod);
        a = mul_mod(a, a, mod);
        e >>= 1;
    }
    return r;
}

static bool is_prime64(u64 n) {
    if (n < 2) return false;
    static const u64 small[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (u64 p : small) {
        if (n == p) return true;
        if (n % p == 0) return false;
    }
    u64 d = n - 1, s = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        ++s;
    }
    for (u64 a : small) {
        if (a >= n) continue;
        u64 x = pow_mod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool comp = true;
        for (u64 r = 1; r < s; ++r) {
            x = mul_mod(x, x, n);
            if (x == n - 1) {
                comp = false;
                break;
            }
        }
        if (comp) return false;
    }
    return true;
}

static u64 gcd64(u64 a, u64 b) {
    while (b) {
        u64 t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static u64 pollard(u64 n) {
    if ((n & 1) == 0) return 2;
    static std::mt19937_64 rng(0x647647647ULL);
    while (true) {
        u64 c = std::uniform_int_distribution<u64>(1, n - 1)(rng);
        u64 x = std::uniform_int_distribution<u64>(0, n - 1)(rng);
        u64 y = x;
        u64 d = 1;
        auto f = [&](u64 v) { return (mul_mod(v, v, n) + c) % n; };
        for (int iter = 0; d == 1; ++iter) {
            x = f(x);
            y = f(f(y));
            u64 diff = x > y ? x - y : y - x;
            d = gcd64(diff, n);
            if (iter > 20000) break;
        }
        if (d > 1 && d < n) return d;
    }
}

static void factor_rec(u64 n, std::vector<u64>& out) {
    if (n == 1) return;
    if (is_prime64(n)) {
        out.push_back(n);
        return;
    }
    u64 d = pollard(n);
    factor_rec(d, out);
    factor_rec(n / d, out);
}

static uint32_t tau64(u64 n) {
    static const int trial_primes[] = {
        2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
        101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,
        193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,
        293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,
        409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,
        521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,
        641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,
        757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,
        881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997
    };
    uint32_t ans = 1;
    for (int pp : trial_primes) {
        u64 p = (u64)pp;
        if (p * p > n) break;
        if (n % p == 0) {
            uint32_t e = 0;
            do {
                n /= p;
                ++e;
            } while (n % p == 0);
            ans *= (e + 1);
        }
    }
    if (n == 1) return ans;
    std::vector<u64> f;
    factor_rec(n, f);
    std::sort(f.begin(), f.end());
    for (size_t i = 0; i < f.size();) {
        size_t j = i + 1;
        while (j < f.size() && f[j] == f[i]) ++j;
        ans *= static_cast<uint32_t>(j - i + 1);
        i = j;
    }
    return ans;
}

static std::vector<int> prime_sieve(int limit) {
    std::vector<bool> comp(limit + 1);
    std::vector<int> primes;
    for (int i = 2; i <= limit; ++i) {
        if (!comp[i]) primes.push_back(i);
        for (int p : primes) {
            long long v = 1LL * i * p;
            if (v > limit) break;
            comp[(int)v] = true;
            if (i % p == 0) break;
        }
    }
    return primes;
}

static int inv_mod(int a, int p) {
    int64_t t = 0, nt = 1, r = p, nr = a % p;
    while (nr) {
        int64_t q = r / nr;
        int64_t tmp = t - q * nt;
        t = nt;
        nt = tmp;
        tmp = r - q * nr;
        r = nr;
        nr = tmp;
    }
    if (t < 0) t += p;
    return (int)t;
}

struct TauRecord {
    uint32_t tau = 1;
    u64 arg = 1;
};

static const int hc_primes[] = {
    2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73
};

static void max_tau_dfs(int idx, int max_exp, u64 cur, uint64_t divs, u64 limit, TauRecord& best) {
    if (divs > best.tau || (divs == best.tau && cur < best.arg)) {
        best.tau = (uint32_t)divs;
        best.arg = cur;
    }
    if (idx >= (int)(sizeof(hc_primes) / sizeof(hc_primes[0]))) return;
    u64 p = (u64)hc_primes[idx];
    u64 x = cur;
    for (int e = 1; e <= max_exp; ++e) {
        if (x > limit / p) break;
        x *= p;
        max_tau_dfs(idx + 1, e, x, divs * (uint64_t)(e + 1), limit, best);
    }
}

static TauRecord max_tau_leq(u64 limit) {
    TauRecord best;
    max_tau_dfs(0, 64, 1, 1, limit, best);
    return best;
}

static bool verify_shifts(u64 n, uint32_t limit, bool verbose) {
    uint32_t worst = 0;
    u64 worst_k = 0;
    for (uint32_t k = 1; k <= limit; ++k) {
        uint32_t t = tau64(n - k);
        if (t > worst) {
            worst = t;
            worst_k = k;
        }
        if (t > k + 2) {
            if (verbose) {
                std::cout << "FAIL n=" << n << " k=" << k
                          << " m=" << (n - k) << " tau=" << t
                          << " bound=" << (k + 2) << "\n";
            }
            return false;
        }
    }
    if (verbose) {
        std::cout << "PASS_SHIFTS n=" << n << " checked_k=" << limit
                  << " worst_tau=" << worst << " at_k=" << worst_k << "\n";
    }
    return true;
}

static uint32_t first_failing_shift(u64 n, uint32_t limit, uint32_t* tau_out = nullptr) {
    for (uint32_t k = 1; k <= limit; ++k) {
        uint32_t t = tau64(n - k);
        if (t > k + 2) {
            if (tau_out) *tau_out = t;
            return k;
        }
    }
    if (tau_out) *tau_out = 0;
    return 0;
}

struct Args {
    u64 start = 1;
    u64 count = 1000000;
    uint32_t segment = 1000000;
    int sieve_limit = 1000000;
    uint32_t quick_shift = 1000;
    bool full = true;
    bool verbose = false;
    bool print_fails = false;
    bool progress = false;
    uint32_t report_survive = 0;
    u64 require_mod = 1;
    u64 require_rem = 0;
    u64 variable_mod = 1;
    u64 variable_rem = 0;
    std::vector<u64> extra_prime_coeffs;
};

static u64 parse_u64(const std::string& s) {
    return std::stoull(s);
}

static Args parse_args(int argc, char** argv) {
    Args a;
    for (int i = 1; i < argc; ++i) {
        std::string key = argv[i];
        auto need = [&]() -> std::string {
            if (++i >= argc) {
                std::cerr << "missing value for " << key << "\n";
                std::exit(2);
            }
            return argv[i];
        };
        if (key == "--start") a.start = parse_u64(need());
        else if (key == "--count") a.count = parse_u64(need());
        else if (key == "--segment") a.segment = (uint32_t)parse_u64(need());
        else if (key == "--sieve-limit") a.sieve_limit = (int)parse_u64(need());
        else if (key == "--quick-shift") a.quick_shift = (uint32_t)parse_u64(need());
        else if (key == "--no-full") a.full = false;
        else if (key == "--verbose") a.verbose = true;
        else if (key == "--print-fails") a.print_fails = true;
        else if (key == "--progress") a.progress = true;
        else if (key == "--report-survive") a.report_survive = (uint32_t)parse_u64(need());
        else if (key == "--require-mod") a.require_mod = parse_u64(need());
        else if (key == "--require-rem") a.require_rem = parse_u64(need());
        else if (key == "--variable-mod") a.variable_mod = parse_u64(need());
        else if (key == "--variable-rem") a.variable_rem = parse_u64(need());
        else if (key == "--extra-prime-coeffs") {
            std::stringstream ss(need());
            std::string part;
            while (std::getline(ss, part, ',')) {
                if (!part.empty()) a.extra_prime_coeffs.push_back(parse_u64(part));
            }
        }
        else {
            std::cerr << "unknown arg " << key << "\n";
            std::exit(2);
        }
    }
    return a;
}

static bool check_extra_prime_coeffs(u64 N, const std::vector<u64>& coeffs) {
    for (u64 c : coeffs) {
        if (N > (std::numeric_limits<u64>::max() - 1) / c) return false;
        if (!is_prime64(c * N - 1)) return false;
    }
    return true;
}

static bool branch_a_prime_tuple(u64 N, const std::vector<u64>& extra_coeffs) {
    // Branch A: n=2520N, N even.
    static const u64 coeff[] = {210,315,420,630,840,1260,2520};
    if (N & 1) return false;
    for (u64 c : coeff) {
        if (!is_prime64(c * N - 1)) return false;
    }
    if (!check_extra_prime_coeffs(N, extra_coeffs)) return false;
    return true;
}

static bool branch_b_prime_tuple(u64 N, const std::vector<u64>& extra_coeffs) {
    // Branch B: n=2520N, N odd. The 315N-1 form is twice a prime.
    static const u64 coeff[] = {210,420,630,840,1260,2520};
    if ((N & 1) == 0) return false;
    if (!is_prime64((315 * N - 1) / 2)) return false;
    for (u64 c : coeff) {
        if (!is_prime64(c * N - 1)) return false;
    }
    if (!check_extra_prime_coeffs(N, extra_coeffs)) return false;
    return true;
}

struct AffineForm {
    u64 a;
    int64_t b;
};

struct RootInfo {
    int p;
    std::vector<int> roots;
};

static RootInfo compute_roots_for_prime(int p, const std::vector<AffineForm>& forms) {
    RootInfo info;
    info.p = p;
    info.roots.reserve(forms.size());
    for (const auto& form : forms) {
        int am = (int)(form.a % (u64)p);
        int bm = (int)(form.b % (int64_t)p);
        if (bm < 0) bm += p;
        if (am == 0) {
            if (bm == 0) {
                info.roots.clear();
                for (int r = 0; r < p; ++r) info.roots.push_back(r);
                return info;
            }
            continue;
        }
        int root = (int)(((u64)(p - bm) * (u64)inv_mod(am, p)) % (u64)p);
        info.roots.push_back(root);
    }
    std::sort(info.roots.begin(), info.roots.end());
    info.roots.erase(std::unique(info.roots.begin(), info.roots.end()), info.roots.end());
    return info;
}

static void mark_roots(std::vector<uint8_t>& alive, u64 seg_start, uint32_t len,
                       const RootInfo& info) {
    const u64 p = (u64)info.p;
    for (int root : info.roots) {
        u64 rem = seg_start % (u64)p;
        u64 off = ((u64)root + (u64)p - rem) % (u64)p;
        for (u64 j = off; j < len; j += (u64)p) alive[(size_t)j] = 0;
    }
}

int main(int argc, char** argv) {
    Args args = parse_args(argc, argv);
    auto primes = prime_sieve(args.sieve_limit);
    std::vector<u64> coeffs = {210,315,420,630,840,1260,2520};
    for (u64 c : args.extra_prime_coeffs) {
        coeffs.push_back(c);
    }
    std::vector<AffineForm> forms;
    for (u64 c : coeffs) {
        forms.push_back({c * args.variable_mod, (int64_t)(c * args.variable_rem) - 1});
    }
    std::vector<RootInfo> root_infos;
    root_infos.reserve(primes.size());
    for (int p : primes) {
        if (p == 2) continue;
        root_infos.push_back(compute_roots_for_prime(p, forms));
    }
    u64 end = args.start + args.count;
    uint64_t tuple_count = 0;
    uint64_t quick_pass_count = 0;
    auto t0 = std::chrono::steady_clock::now();

    for (u64 base = args.start; base < end; base += args.segment) {
        uint32_t len = (uint32_t)std::min<u64>(args.segment, end - base);
        std::vector<uint8_t> alive(len, 1);

        for (const auto& info : root_infos) {
            mark_roots(alive, base, len, info);
        }

        for (uint32_t i = 0; i < len; ++i) {
            if (!alive[i]) continue;
            u64 X = base + i;
            u64 N = args.variable_mod * X + args.variable_rem;
            if (args.require_mod != 1 && N % args.require_mod != args.require_rem) continue;
            int branch = 0;
            if ((N & 1) == 0 && branch_a_prime_tuple(N, args.extra_prime_coeffs)) branch = 1;
            if (!branch && (N & 1) == 1 && branch_b_prime_tuple(N, args.extra_prime_coeffs)) branch = 2;
            if (!branch) continue;

            ++tuple_count;
            u64 n = 2520 * N;
            if (args.verbose) {
                std::cout << "PRIME_TUPLE branch=" << (branch == 1 ? "A" : "B")
                          << " N=" << N << " n=" << n << "\n";
            }
            uint32_t fail_tau = 0;
            uint32_t fail_k = first_failing_shift(n, args.quick_shift, &fail_tau);
            if (fail_k != 0) {
                if (args.print_fails) {
                    std::cout << "FAIL n=" << n << " k=" << fail_k
                              << " m=" << (n - fail_k) << " tau=" << fail_tau
                              << " bound=" << (fail_k + 2) << "\n";
                }
                if (args.report_survive && fail_k > args.report_survive) {
                    std::cout << "SURVIVE branch=" << (branch == 1 ? "A" : "B")
                              << " N=" << N << " n=" << n
                              << " first_fail_k=" << fail_k
                              << " fail_tau=" << fail_tau << "\n";
                }
                continue;
            }
            ++quick_pass_count;
            std::cout << "QUICK_PASS branch=" << (branch == 1 ? "A" : "B")
                      << " N=" << N << " n=" << n
                      << " checked_k=" << args.quick_shift << "\n";

            if (args.full) {
                TauRecord rec = max_tau_leq(n - 1);
                uint32_t full_limit = rec.tau > 2 ? rec.tau - 2 : 1;
                std::cout << "MAX_TAU_BOUND n=" << n << " max_tau=" << rec.tau
                          << " at_m=" << rec.arg
                          << " full_shift_limit=" << full_limit << "\n";
                if (verify_shifts(n, full_limit, true)) {
                    std::cout << "CANDIDATE n=" << n << " N=" << N
                              << " branch=" << (branch == 1 ? "A" : "B")
                              << " max_tau_bound=" << rec.tau
                              << " max_tau_arg=" << rec.arg << "\n";
                    return 0;
                }
            }
        }

        if (args.progress) {
            auto now = std::chrono::steady_clock::now();
            double sec = std::chrono::duration<double>(now - t0).count();
            std::cerr << "segment_done base=" << base << " len=" << len
                      << " tuples=" << tuple_count
                      << " quick_pass=" << quick_pass_count
                      << " elapsed=" << sec << "s\n";
        }
    }
    std::cout << "DONE start=" << args.start << " count=" << args.count
              << " prime_tuples=" << tuple_count
              << " quick_pass=" << quick_pass_count << "\n";
    return 0;
}
