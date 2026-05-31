#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

static const uint32_t primes[] = {2,3,5,7,11,13,17,19};
static const uint32_t emax[] = {3,2,1,1,1,1,1,1};

struct ForcedData {
    uint32_t tau = 1;
    uint32_t exp[8] = {};
};

static ForcedData forced_data(uint64_t x) {
    ForcedData data;
    for (int i = 0; i < 8; ++i) {
        uint32_t e = 0;
        while (e < emax[i] && x % primes[i] == 0) {
            x /= primes[i];
            ++e;
        }
        data.exp[i] = e;
        data.tau *= e + 1;
    }
    return data;
}

static uint64_t max_forced_smooth(const ForcedData& data, uint32_t tau_bound, uint64_t cap) {
    std::vector<int> idxs;
    uint64_t forced_part = 1;
    for (int i = 0; i < 8; ++i) {
        if (data.exp[i] == 0) continue;
        idxs.push_back(i);
        for (uint32_t e = 0; e < data.exp[i]; ++e) {
            if (forced_part > cap / primes[i]) return cap;
            forced_part *= primes[i];
        }
    }
    if (idxs.empty()) return 1;
    uint64_t best = 0;

    auto dfs = [&](auto&& self, size_t pos, uint64_t cur, uint32_t divs) -> void {
        if (pos == idxs.size()) {
            if (cur > best) best = cur;
            return;
        }
        int i = idxs[pos];
        uint32_t base_exp = data.exp[i];
        uint64_t x = cur;
        for (uint32_t e = base_exp; ; ++e) {
            uint32_t next_divs = divs / (base_exp + 1) * (e + 1);
            if (next_divs > tau_bound) break;
            self(self, pos + 1, x, next_divs);
            if (x > cap / primes[i]) break;
            x *= primes[i];
        }
    };

    dfs(dfs, 0, forced_part, data.tau);
    return best;
}

static uint32_t tau_gcd_known(uint64_t x) {
    uint32_t ans = 1;
    for (int i = 0; i < 8; ++i) {
        uint32_t e = 0;
        while (e < emax[i] && x % primes[i] == 0) {
            x /= primes[i];
            ++e;
        }
        ans *= e + 1;
    }
    return ans;
}

int main(int argc, char** argv) {
    uint32_t K = argc > 1 ? (uint32_t)std::stoul(argv[1]) : 200;
    const uint64_t R = 11ull * 13 * 17 * 19;
    const uint64_t Q = 2520ull * R;
    std::vector<uint32_t> good;
    for (uint32_t r = 0; r < R; ++r) {
        bool ok = true;
        for (uint32_t k = 1; k <= K; ++k) {
            uint64_t x = (2520ull * r + Q - (k % Q)) % Q;
            if (x == 0) x = Q;
            ForcedData data = forced_data(x);
            uint32_t bound = k + 2;
            if (data.tau > bound) {
                ok = false;
                break;
            }
            if (2 * data.tau > bound) {
                uint64_t max_smooth = max_forced_smooth(data, bound, Q);
                if (x > max_smooth) {
                    ok = false;
                    break;
                }
            }
        }
        if (ok) good.push_back(r);
    }
    std::cout << "K " << K << " count " << good.size() << "\n";
    for (size_t i = 0; i < good.size(); ++i) {
        if (i) std::cout << (i % 16 == 0 ? "\n" : " ");
        std::cout << good[i];
    }
    std::cout << "\n";
    return 0;
}
