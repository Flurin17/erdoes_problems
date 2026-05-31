#include <algorithm>
#include <chrono>
#include <cctype>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <random>
#include <sstream>
#include <string>
#include <vector>

using u64 = uint64_t;
using u128 = __uint128_t;
using i128 = __int128_t;

static constexpr u128 U128_MAX_VALUE = ~u128(0);
static constexpr u128 I128_MAX_AS_U128 = U128_MAX_VALUE >> 1;
static constexpr i128 I128_MAX_VALUE = (i128)I128_MAX_AS_U128;
static constexpr i128 I128_MIN_VALUE = -I128_MAX_VALUE - 1;

[[noreturn]] static void die(const std::string& msg) {
    std::cerr << msg << "\n";
    std::exit(2);
}

static std::string u128_to_string(u128 v) {
    if (v == 0) return "0";
    std::string out;
    while (v) {
        int digit = (int)(v % 10);
        out.push_back((char)('0' + digit));
        v /= 10;
    }
    std::reverse(out.begin(), out.end());
    return out;
}

static u128 i128_abs_to_u128(i128 v) {
    if (v >= 0) return (u128)v;
    return (u128)(-(v + 1)) + 1;
}

static std::string i128_to_string(i128 v) {
    if (v >= 0) return u128_to_string((u128)v);
    return "-" + u128_to_string(i128_abs_to_u128(v));
}

static u128 parse_u128(const std::string& s) {
    if (s.empty()) die("empty unsigned integer");
    u128 v = 0;
    for (char ch : s) {
        if (!std::isdigit((unsigned char)ch)) {
            die("invalid unsigned integer: " + s);
        }
        u128 d = (u128)(ch - '0');
        if (v > (U128_MAX_VALUE - d) / 10) {
            die("unsigned integer overflows 128 bits: " + s);
        }
        v = v * 10 + d;
    }
    return v;
}

static i128 parse_i128(const std::string& s) {
    if (s.empty()) die("empty signed integer");
    bool neg = false;
    size_t pos = 0;
    if (s[0] == '+' || s[0] == '-') {
        neg = s[0] == '-';
        pos = 1;
    }
    if (pos == s.size()) die("invalid signed integer: " + s);
    u128 mag = 0;
    for (; pos < s.size(); ++pos) {
        char ch = s[pos];
        if (!std::isdigit((unsigned char)ch)) {
            die("invalid signed integer: " + s);
        }
        u128 d = (u128)(ch - '0');
        if (mag > (U128_MAX_VALUE - d) / 10) {
            die("signed integer overflows 128 bits: " + s);
        }
        mag = mag * 10 + d;
    }

    u128 limit = neg ? I128_MAX_AS_U128 + 1 : I128_MAX_AS_U128;
    if (mag > limit) die("signed integer outside int128 range: " + s);
    if (!neg) return (i128)mag;
    if (mag == I128_MAX_AS_U128 + 1) return I128_MIN_VALUE;
    return -(i128)mag;
}

static uint32_t parse_u32(const std::string& s, const std::string& name) {
    u128 v = parse_u128(s);
    if (v > (u128)std::numeric_limits<uint32_t>::max()) {
        die(name + " exceeds uint32_t range");
    }
    return (uint32_t)v;
}

static int parse_int(const std::string& s, const std::string& name) {
    u128 v = parse_u128(s);
    if (v > (u128)std::numeric_limits<int>::max()) {
        die(name + " exceeds int range");
    }
    return (int)v;
}

static bool checked_add(u128 a, u128 b, u128& out) {
    if (a > U128_MAX_VALUE - b) return false;
    out = a + b;
    return true;
}

static bool checked_mul(u128 a, u128 b, u128& out) {
    if (a != 0 && b > U128_MAX_VALUE / a) return false;
    out = a * b;
    return true;
}

static i128 u128_to_i128_checked(u128 v, const std::string& what) {
    if (v > I128_MAX_AS_U128) {
        die(what + " does not fit in signed int128");
    }
    return (i128)v;
}

static std::vector<int> prime_sieve(int limit) {
    if (limit < 2) return {};
    std::vector<bool> comp((size_t)limit + 1);
    std::vector<int> primes;
    for (int i = 2; i <= limit; ++i) {
        if (!comp[(size_t)i]) primes.push_back(i);
        for (int p : primes) {
            long long v = 1LL * i * p;
            if (v > limit) break;
            comp[(size_t)v] = true;
            if (i % p == 0) break;
        }
    }
    return primes;
}

static u128 add_mod(u128 a, u128 b, u128 mod) {
    a %= mod;
    b %= mod;
    if (a >= mod - b) return a - (mod - b);
    return a + b;
}

static u128 mul_mod(u128 a, u128 b, u128 mod) {
    a %= mod;
    b %= mod;
    if (a == 0 || b <= U128_MAX_VALUE / a) return (a * b) % mod;
    u128 r = 0;
    while (b) {
        if (b & 1) r = add_mod(r, a, mod);
        b >>= 1;
        if (b) a = add_mod(a, a, mod);
    }
    return r;
}

static u128 pow_mod(u128 a, u128 e, u128 mod) {
    u128 r = 1;
    while (e) {
        if (e & 1) r = mul_mod(r, a, mod);
        a = mul_mod(a, a, mod);
        e >>= 1;
    }
    return r;
}

static u128 gcd128(u128 a, u128 b) {
    while (b) {
        u128 t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static bool is_prime128(u128 n) {
    if (n < 2) return false;
    static const u64 trial[] = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    };
    for (u64 p : trial) {
        if (n == (u128)p) return true;
        if (n % (u128)p == 0) return false;
    }

    u128 d = n - 1;
    uint32_t s = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        ++s;
    }

    // First 12 prime bases are deterministic beyond the requested 1e22 range;
    // the remaining bases are cheap extra screening for this experimental tool.
    static const u64 bases[] = {
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    };
    for (u64 a64 : bases) {
        u128 a = (u128)a64;
        if (a >= n) continue;
        u128 x = pow_mod(a, d, n);
        if (x == 1 || x == n - 1) continue;
        bool composite = true;
        for (uint32_t r = 1; r < s; ++r) {
            x = mul_mod(x, x, n);
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}

static u128 abs_diff(u128 a, u128 b) {
    return a > b ? a - b : b - a;
}

static u128 random_u128(std::mt19937_64& rng) {
    return ((u128)rng() << 64) ^ (u128)rng();
}

static u128 random_range(std::mt19937_64& rng, u128 lo, u128 hi) {
    return lo + random_u128(rng) % (hi - lo + 1);
}

static u128 pollard(u128 n) {
    if ((n & 1) == 0) return 2;
    if (n % 3 == 0) return 3;
    if (n % 5 == 0) return 5;

    static std::mt19937_64 rng(0x647647647ULL);
    while (true) {
        u128 c = random_range(rng, 1, n - 1);
        u128 x = random_range(rng, 2, n - 2);
        u128 y = x;
        u128 d = 1;
        auto f = [&](u128 v) { return add_mod(mul_mod(v, v, n), c, n); };
        for (int iter = 0; d == 1 && iter < 200000; ++iter) {
            x = f(x);
            y = f(f(y));
            d = gcd128(abs_diff(x, y), n);
        }
        if (d > 1 && d < n) return d;
    }
}

static void factor_rec(u128 n, std::vector<u128>& out) {
    if (n == 1) return;
    if (is_prime128(n)) {
        out.push_back(n);
        return;
    }
    u128 d = pollard(n);
    factor_rec(d, out);
    factor_rec(n / d, out);
}

static uint64_t tau128(u128 n) {
    if (n == 0) return 0;
    uint64_t ans = 1;
    static const std::vector<int> trial_primes = prime_sieve(997);
    for (int pp : trial_primes) {
        u128 p = (u128)pp;
        if (p * p > n) break;
        if (n % p == 0) {
            uint64_t e = 0;
            do {
                n /= p;
                ++e;
            } while (n % p == 0);
            ans *= (e + 1);
        }
    }
    if (n == 1) return ans;
    std::vector<u128> f;
    factor_rec(n, f);
    std::sort(f.begin(), f.end());
    for (size_t i = 0; i < f.size();) {
        size_t j = i + 1;
        while (j < f.size() && f[j] == f[i]) ++j;
        ans *= (uint64_t)(j - i + 1);
        i = j;
    }
    return ans;
}

static u128 isqrt128(u128 n) {
    u128 lo = 0;
    u128 hi = (u128)std::numeric_limits<u64>::max() + 1;
    while (lo + 1 < hi) {
        u128 mid = lo + (hi - lo) / 2;
        if (mid * mid <= n) lo = mid;
        else hi = mid;
    }
    return lo;
}

static u128 icbrt128(u128 n) {
    u128 lo = 0;
    u128 hi = (u128)1 << 43;
    while (lo + 1 < hi) {
        u128 mid = lo + (hi - lo) / 2;
        if (mid * mid * mid <= n) lo = mid;
        else hi = mid;
    }
    return lo;
}

static bool tau_leq_small(u128 n, uint32_t bound) {
    if (bound == 0) return false;
    uint32_t known = 1;
    static const std::vector<int> trial_primes = prime_sieve(97);
    for (int pp : trial_primes) {
        u128 p = (u128)pp;
        if (p * p > n) break;
        if (n % p == 0) {
            uint32_t e = 0;
            do {
                n /= p;
                ++e;
            } while (n % p == 0);
            known *= e + 1;
            if (known > bound) return false;
        }
    }
    bound /= known;
    if (n == 1) return true;
    if (bound == 1) return false;
    if (is_prime128(n)) return true;
    if (bound == 2) return false;

    u128 root = isqrt128(n);
    if (root * root == n && is_prime128(root)) return true;
    if (bound == 3) return false;

    u128 cube = icbrt128(n);
    if (cube * cube * cube == n && is_prime128(cube)) return true;

    std::vector<u128> factors;
    factor_rec(n, factors);
    if (factors.size() != 2) return false;
    return is_prime128(factors[0]) && is_prime128(factors[1]);
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
    uint64_t tau = 1;
    u128 arg = 1;
};

static const int hc_primes[] = {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
    37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
    79, 83, 89, 97, 101, 103, 107, 109, 113, 127
};

static void max_tau_dfs(int idx, int max_exp, u128 cur, uint64_t divs,
                        u128 limit, TauRecord& best) {
    if (divs > best.tau || (divs == best.tau && cur < best.arg)) {
        best.tau = divs;
        best.arg = cur;
    }
    if (idx >= (int)(sizeof(hc_primes) / sizeof(hc_primes[0]))) return;
    u128 p = (u128)hc_primes[idx];
    u128 x = cur;
    for (int e = 1; e <= max_exp; ++e) {
        if (x > limit / p) break;
        x *= p;
        max_tau_dfs(idx + 1, e, x, divs * (uint64_t)(e + 1), limit, best);
    }
}

static TauRecord max_tau_leq(u128 limit) {
    TauRecord best;
    max_tau_dfs(0, 128, 1, 1, limit, best);
    return best;
}

static bool coeff_minus_one(u128 coeff, u128 N, u128& out) {
    u128 prod = 0;
    if (!checked_mul(coeff, N, prod)) return false;
    if (prod == 0) return false;
    out = prod - 1;
    return true;
}

static bool coeff_times(u128 coeff, u128 N, u128& out) {
    return checked_mul(coeff, N, out);
}

static bool verify_shifts(u128 n, uint32_t limit, bool verbose) {
    uint64_t worst = 0;
    uint32_t worst_k = 0;
    for (uint32_t k = 1; k <= limit && (u128)k < n; ++k) {
        uint64_t t = tau128(n - (u128)k);
        if (t > worst) {
            worst = t;
            worst_k = k;
        }
        if (t > (uint64_t)k + 2) {
            if (verbose) {
                std::cout << "FAIL n=" << u128_to_string(n)
                          << " k=" << k
                          << " m=" << u128_to_string(n - (u128)k)
                          << " tau=" << t
                          << " bound=" << ((uint64_t)k + 2) << "\n";
            }
            return false;
        }
    }
    if (verbose) {
        std::cout << "PASS_SHIFTS n=" << u128_to_string(n)
                  << " checked_k=" << limit
                  << " worst_tau=" << worst
                  << " at_k=" << worst_k << "\n";
    }
    return true;
}

static bool power_prime_budget_ok(u128 L, u128 p, uint32_t fixed_exp,
                                  uint32_t other_tau, uint32_t bound) {
    if (L == 0) return false;
    uint32_t a = 0;
    while (L % p == 0) {
        L /= p;
        ++a;
    }
    uint32_t fixed_part = fixed_exp + a + 1;
    if (L == 1) return other_tau * fixed_part <= bound;
    if (other_tau * fixed_part * 2 > bound) return false;
    return is_prime128(L);
}

static bool shared_prime_budget_ok(u128 L, u128 p, uint32_t fixed_exp,
                                   uint32_t other_tau, uint32_t bound) {
    if (L == 0) return false;
    uint32_t a = 0;
    while (L % p == 0) {
        L /= p;
        ++a;
    }
    uint32_t fixed_part = fixed_exp + a + 1;
    uint32_t forced_tau = other_tau * fixed_part;
    if (forced_tau > bound) return false;
    return tau_leq_small(L, bound / forced_tau);
}

static bool shift5_ok(u128 N) {
    u128 L = 0;
    return coeff_minus_one(504, N, L) && power_prime_budget_ok(L, 5, 1, 1, 7);
}

static bool shift9_ok(u128 N) {
    u128 L = 0;
    return coeff_minus_one(280, N, L) && power_prime_budget_ok(L, 3, 2, 1, 11);
}

static bool shift10_ok(u128 N) {
    u128 L = 0;
    return coeff_minus_one(252, N, L) && power_prime_budget_ok(L, 5, 1, 2, 12);
}

static bool shift7_ok(u128 N) {
    u128 L = 0;
    return coeff_minus_one(360, N, L) && shared_prime_budget_ok(L, 7, 1, 1, 9);
}

static bool shift14_ok(u128 N) {
    u128 L = 0;
    return coeff_minus_one(180, N, L) && shared_prime_budget_ok(L, 7, 1, 2, 16);
}

static bool shift15_ok(u128 N) {
    u128 L = 0;
    return coeff_minus_one(168, N, L) && shared_prime_budget_ok(L, 5, 1, 2, 17);
}

static bool shift16_ok(u128 N) {
    u128 L = 0;
    if (!checked_mul(315, N, L) || L < 2) return false;
    L -= 2;
    return shared_prime_budget_ok(L, 2, 3, 1, 18);
}

static bool guaranteed_by_branch(uint32_t k, int branch) {
    if (k == 1 || k == 2 || k == 3 || k == 4 || k == 6 || k == 8 || k == 12) {
        return true;
    }
    if (branch == 1 && k == 24) return true;
    return false;
}

static uint32_t first_failing_shift(u128 n, u128 N, int branch, uint32_t limit,
                                    uint64_t* tau_out = nullptr) {
    for (uint32_t k = 1; k <= limit && (u128)k < n; ++k) {
        if (guaranteed_by_branch(k, branch)) continue;
        if (k == 5) {
            if (shift5_ok(N)) continue;
            if (tau_out) *tau_out = tau128(n - (u128)k);
            return k;
        }
        if (k == 7) {
            if (shift7_ok(N)) continue;
            if (tau_out) *tau_out = tau128(n - (u128)k);
            return k;
        }
        if (k == 9) {
            if (shift9_ok(N)) continue;
            if (tau_out) *tau_out = tau128(n - (u128)k);
            return k;
        }
        if (k == 10) {
            if (shift10_ok(N)) continue;
            if (tau_out) *tau_out = tau128(n - (u128)k);
            return k;
        }
        if (k == 14) {
            if (shift14_ok(N)) continue;
            if (tau_out) *tau_out = tau128(n - (u128)k);
            return k;
        }
        if (k == 15) {
            if (shift15_ok(N)) continue;
            if (tau_out) *tau_out = tau128(n - (u128)k);
            return k;
        }
        if (k == 16) {
            if (shift16_ok(N)) continue;
            if (tau_out) *tau_out = tau128(n - (u128)k);
            return k;
        }
        uint64_t t = tau128(n - (u128)k);
        if (t > (uint64_t)k + 2) {
            if (tau_out) *tau_out = t;
            return k;
        }
    }
    if (tau_out) *tau_out = 0;
    return 0;
}

struct AffineForm {
    u128 a;
    i128 b;
};

static bool eval_affine_u128(const AffineForm& form, u128 x, u128& out) {
    u128 prod = 0;
    if (!checked_mul(form.a, x, prod)) return false;
    if (form.b >= 0) {
        return checked_add(prod, (u128)form.b, out);
    }
    u128 mag = i128_abs_to_u128(form.b);
    if (prod < mag) return false;
    out = prod - mag;
    return true;
}

struct Args {
    u128 start = 1;
    u128 count = 1000000;
    uint32_t segment = 1000000;
    int sieve_limit = 1000000;
    uint32_t quick_shift = 1000;
    bool full = true;
    bool verbose = false;
    bool print_fails = false;
    bool progress = false;
    bool stats = false;
    uint32_t report_survive = 0;
    u128 require_mod = 1;
    u128 require_rem = 0;
    u128 variable_mod = 1;
    u128 variable_rem = 0;
    std::vector<u128> extra_prime_coeffs;
    std::vector<AffineForm> extra_prime_forms;
};

static Args parse_args(int argc, char** argv) {
    Args a;
    for (int i = 1; i < argc; ++i) {
        std::string key = argv[i];
        auto need = [&]() -> std::string {
            if (++i >= argc) die("missing value for " + key);
            return argv[i];
        };
        if (key == "--start") a.start = parse_u128(need());
        else if (key == "--count") a.count = parse_u128(need());
        else if (key == "--segment") a.segment = parse_u32(need(), "--segment");
        else if (key == "--sieve-limit") a.sieve_limit = parse_int(need(), "--sieve-limit");
        else if (key == "--quick-shift") a.quick_shift = parse_u32(need(), "--quick-shift");
        else if (key == "--no-full") a.full = false;
        else if (key == "--verbose") a.verbose = true;
        else if (key == "--print-fails") a.print_fails = true;
        else if (key == "--progress") a.progress = true;
        else if (key == "--stats") a.stats = true;
        else if (key == "--report-survive") a.report_survive = parse_u32(need(), "--report-survive");
        else if (key == "--require-mod") a.require_mod = parse_u128(need());
        else if (key == "--require-rem") a.require_rem = parse_u128(need());
        else if (key == "--variable-mod") a.variable_mod = parse_u128(need());
        else if (key == "--variable-rem") a.variable_rem = parse_u128(need());
        else if (key == "--extra-prime-coeffs") {
            std::stringstream ss(need());
            std::string part;
            while (std::getline(ss, part, ',')) {
                if (!part.empty()) a.extra_prime_coeffs.push_back(parse_u128(part));
            }
        }
        else if (key == "--extra-prime-forms") {
            std::stringstream ss(need());
            std::string part;
            while (std::getline(ss, part, ',')) {
                if (part.empty()) continue;
                size_t colon = part.find(':');
                if (colon == std::string::npos) {
                    die("extra prime forms must be A:B pairs");
                }
                u128 aa = parse_u128(part.substr(0, colon));
                i128 bb = parse_i128(part.substr(colon + 1));
                a.extra_prime_forms.push_back({aa, bb});
            }
        }
        else {
            die("unknown arg " + key);
        }
    }
    if (a.segment == 0) die("--segment must be positive");
    if (a.require_mod == 0) die("--require-mod must be positive");
    return a;
}

static bool make_N_coeff_form(u128 coeff, const Args& args, AffineForm& out) {
    u128 slope = 0;
    if (!checked_mul(coeff, args.variable_mod, slope)) return false;
    u128 rem_part = 0;
    if (!checked_mul(coeff, args.variable_rem, rem_part)) return false;
    i128 b = -1;
    if (rem_part > 0) {
        b = u128_to_i128_checked(rem_part - 1, "affine intercept");
    }
    out = {slope, b};
    return true;
}

static bool check_prime_coeff(u128 coeff, u128 N) {
    u128 value = 0;
    return coeff_minus_one(coeff, N, value) && is_prime128(value);
}

static bool check_extra_prime_coeffs(u128 N, const std::vector<u128>& coeffs) {
    for (u128 c : coeffs) {
        if (!check_prime_coeff(c, N)) return false;
    }
    return true;
}

static bool check_extra_prime_forms(u128 X, const std::vector<AffineForm>& forms) {
    for (const auto& form : forms) {
        u128 value = 0;
        if (!eval_affine_u128(form, X, value)) return false;
        if (!is_prime128(value)) return false;
    }
    return true;
}

static bool branch_a_prime_tuple(u128 N, const std::vector<u128>& extra_coeffs) {
    static const u64 coeff[] = {105, 210, 315, 420, 630, 840, 1260, 2520};
    if (N & 1) return false;
    for (u64 c : coeff) {
        if (!check_prime_coeff((u128)c, N)) return false;
    }
    return check_extra_prime_coeffs(N, extra_coeffs);
}

static bool branch_b_prime_tuple(u128 N, const std::vector<u128>& extra_coeffs) {
    static const u64 coeff[] = {210, 420, 630, 840, 1260, 2520};
    if ((N & 1) == 0) return false;
    u128 value315 = 0;
    if (!coeff_minus_one(315, N, value315)) return false;
    if ((value315 & 1) != 0) return false;
    if (!is_prime128(value315 / 2)) return false;
    for (u64 c : coeff) {
        if (!check_prime_coeff((u128)c, N)) return false;
    }
    return check_extra_prime_coeffs(N, extra_coeffs);
}

struct RootInfo {
    int p = 0;
    std::vector<int> roots;
};

static int mod_i128(i128 x, int p) {
    i128 r = x % (i128)p;
    if (r < 0) r += p;
    return (int)r;
}

static RootInfo compute_roots_for_prime(int p, const std::vector<AffineForm>& forms) {
    RootInfo info;
    info.p = p;
    info.roots.reserve(forms.size());
    for (const auto& form : forms) {
        int am = (int)(form.a % (u128)p);
        int bm = mod_i128(form.b, p);
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

static void mark_roots(std::vector<uint8_t>& alive, u128 seg_start, uint32_t len,
                       const RootInfo& info) {
    const u64 p = (u64)info.p;
    if (p == 0) return;
    u64 rem = (u64)(seg_start % (u128)p);
    for (int root : info.roots) {
        u64 off = ((u64)root + p - rem) % p;
        for (u64 j = off; j < (u64)len; j += p) alive[(size_t)j] = 0;
    }
}

static bool compute_N(const Args& args, u128 X, u128& N) {
    u128 prod = 0;
    if (!checked_mul(args.variable_mod, X, prod)) return false;
    return checked_add(prod, args.variable_rem, N);
}

int main(int argc, char** argv) {
    Args args = parse_args(argc, argv);
    auto primes = prime_sieve(args.sieve_limit);

    std::vector<u128> common_coeffs = {210, 315, 420, 630, 840, 1260, 2520};
    std::vector<u128> branch_a_coeffs = {105};
    for (u128 c : args.extra_prime_coeffs) {
        common_coeffs.push_back(c);
    }

    std::vector<AffineForm> common_forms;
    for (u128 c : common_coeffs) {
        AffineForm form;
        if (!make_N_coeff_form(c, args, form)) die("affine common form overflows uint128");
        common_forms.push_back(form);
    }
    for (const auto& form : args.extra_prime_forms) {
        common_forms.push_back(form);
    }

    std::vector<AffineForm> branch_a_forms;
    for (u128 c : branch_a_coeffs) {
        AffineForm form;
        if (!make_N_coeff_form(c, args, form)) die("affine branch-A form overflows uint128");
        branch_a_forms.push_back(form);
    }

    std::vector<RootInfo> common_root_infos;
    std::vector<RootInfo> branch_a_root_infos;
    common_root_infos.reserve(primes.size());
    branch_a_root_infos.reserve(primes.size());
    for (int p : primes) {
        if (p == 2) continue;
        common_root_infos.push_back(compute_roots_for_prime(p, common_forms));
        branch_a_root_infos.push_back(compute_roots_for_prime(p, branch_a_forms));
    }

    u128 end = 0;
    if (!checked_add(args.start, args.count, end)) die("--start + --count overflows uint128");

    uint64_t tuple_count = 0;
    uint64_t quick_pass_count = 0;
    std::vector<uint64_t> first_fail_counts((size_t)args.quick_shift + 1);
    std::vector<uint64_t> branch_counts(3);
    uint32_t best_fail_k = 0;
    u128 best_fail_n = 0;
    u128 best_fail_N = 0;
    uint64_t best_fail_tau = 0;
    auto t0 = std::chrono::steady_clock::now();

    for (u128 base = args.start; base < end;) {
        u128 remain = end - base;
        uint32_t len = remain < (u128)args.segment ? (uint32_t)remain : args.segment;
        std::vector<uint8_t> alive_common(len, 1);
        std::vector<uint8_t> alive_a(len, 1);

        for (const auto& info : common_root_infos) {
            mark_roots(alive_common, base, len, info);
        }
        alive_a = alive_common;
        for (const auto& info : branch_a_root_infos) {
            mark_roots(alive_a, base, len, info);
        }

        for (uint32_t i = 0; i < len; ++i) {
            u128 X = base + (u128)i;
            u128 N = 0;
            if (!compute_N(args, X, N)) die("N = variable_mod * X + variable_rem overflows uint128");
            if (args.require_mod != 1 && N % args.require_mod != args.require_rem) continue;
            if (!check_extra_prime_forms(X, args.extra_prime_forms)) continue;

            int branch = 0;
            if ((N & 1) == 0 && alive_a[(size_t)i] &&
                branch_a_prime_tuple(N, args.extra_prime_coeffs)) {
                branch = 1;
            }
            if (!branch && (N & 1) == 1 && alive_common[(size_t)i] &&
                branch_b_prime_tuple(N, args.extra_prime_coeffs)) {
                branch = 2;
            }
            if (!branch) continue;

            ++tuple_count;
            ++branch_counts[(size_t)branch];
            u128 n = 0;
            if (!coeff_times(2520, N, n)) die("n = 2520 * N overflows uint128");
            if (args.verbose) {
                std::cout << "PRIME_TUPLE branch=" << (branch == 1 ? "A" : "B")
                          << " N=" << u128_to_string(N)
                          << " n=" << u128_to_string(n) << "\n";
            }

            uint64_t fail_tau = 0;
            uint32_t fail_k = first_failing_shift(n, N, branch, args.quick_shift, &fail_tau);
            if (fail_k != 0) {
                ++first_fail_counts[(size_t)fail_k];
                if (fail_k > best_fail_k) {
                    best_fail_k = fail_k;
                    best_fail_n = n;
                    best_fail_N = N;
                    best_fail_tau = fail_tau;
                }
                if (args.print_fails) {
                    std::cout << "FAIL n=" << u128_to_string(n)
                              << " k=" << fail_k
                              << " m=" << u128_to_string(n - (u128)fail_k)
                              << " tau=" << fail_tau
                              << " bound=" << ((uint64_t)fail_k + 2) << "\n";
                }
                if (args.report_survive && fail_k > args.report_survive) {
                    std::cout << "SURVIVE branch=" << (branch == 1 ? "A" : "B")
                              << " N=" << u128_to_string(N)
                              << " n=" << u128_to_string(n)
                              << " first_fail_k=" << fail_k
                              << " fail_tau=" << fail_tau << "\n";
                }
                continue;
            }

            ++quick_pass_count;
            ++first_fail_counts[0];
            std::cout << "QUICK_PASS branch=" << (branch == 1 ? "A" : "B")
                      << " N=" << u128_to_string(N)
                      << " n=" << u128_to_string(n)
                      << " checked_k=" << args.quick_shift << "\n";

            if (args.full) {
                TauRecord rec = max_tau_leq(n - 1);
                uint32_t full_limit = rec.tau > 2 ? (uint32_t)(rec.tau - 2) : 1;
                std::cout << "MAX_TAU_BOUND n=" << u128_to_string(n)
                          << " max_tau=" << rec.tau
                          << " at_m=" << u128_to_string(rec.arg)
                          << " full_shift_limit=" << full_limit << "\n";
                if (verify_shifts(n, full_limit, true)) {
                    std::cout << "CANDIDATE n=" << u128_to_string(n)
                              << " N=" << u128_to_string(N)
                              << " branch=" << (branch == 1 ? "A" : "B")
                              << " max_tau_bound=" << rec.tau
                              << " max_tau_arg=" << u128_to_string(rec.arg) << "\n";
                    return 0;
                }
            }
        }

        if (args.progress) {
            auto now = std::chrono::steady_clock::now();
            double sec = std::chrono::duration<double>(now - t0).count();
            std::cerr << "segment_done base=" << u128_to_string(base)
                      << " len=" << len
                      << " tuples=" << tuple_count
                      << " quick_pass=" << quick_pass_count
                      << " elapsed=" << sec << "s\n";
        }
        base += (u128)len;
    }

    std::cout << "DONE start=" << u128_to_string(args.start)
              << " count=" << u128_to_string(args.count)
              << " prime_tuples=" << tuple_count
              << " quick_pass=" << quick_pass_count << "\n";
    if (args.stats) {
        std::cout << "BRANCH_COUNTS A=" << branch_counts[1]
                  << " B=" << branch_counts[2] << "\n";
        std::cout << "BEST_FIRST_FAIL k=" << best_fail_k
                  << " N=" << u128_to_string(best_fail_N)
                  << " n=" << u128_to_string(best_fail_n)
                  << " tau=" << best_fail_tau << "\n";
        std::cout << "FIRST_FAIL_COUNTS";
        for (uint32_t k = 0; k < first_fail_counts.size(); ++k) {
            if (first_fail_counts[(size_t)k]) {
                std::cout << " " << k << ":" << first_fail_counts[(size_t)k];
            }
        }
        std::cout << "\n";
    }
    return 0;
}
