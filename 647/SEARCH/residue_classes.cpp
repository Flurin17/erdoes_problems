#include <cstdint>
#include <iostream>
#include <vector>

static uint32_t tau_gcd_known(uint64_t x) {
    static const uint32_t p[] = {2,3,5,7,11,13,17,19};
    static const uint32_t emax[] = {3,2,1,1,1,1,1,1};
    uint32_t ans = 1;
    for (int i = 0; i < 8; ++i) {
        uint32_t e = 0;
        while (e < emax[i] && x % p[i] == 0) {
            x /= p[i];
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
        uint64_t n0 = (2520ull * r) % Q;
        bool ok = true;
        for (uint32_t k = 1; k <= K; ++k) {
            uint64_t x = (n0 + Q - (k % Q)) % Q;
            if (tau_gcd_known(x) > k + 2) {
                ok = false;
                break;
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
