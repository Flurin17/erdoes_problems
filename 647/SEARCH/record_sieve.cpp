#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char** argv) {
    uint32_t limit = 1000000;
    if (argc > 1) limit = (uint32_t)std::stoul(argv[1]);

    std::vector<uint32_t> primes;
    std::vector<uint32_t> lp(limit + 1);
    std::vector<uint16_t> tau(limit + 1);
    std::vector<uint8_t> exp(limit + 1);
    tau[1] = 1;

    for (uint32_t i = 2; i <= limit; ++i) {
        if (lp[i] == 0) {
            lp[i] = i;
            primes.push_back(i);
            tau[i] = 2;
            exp[i] = 1;
        }
        for (uint32_t p : primes) {
            uint64_t v = (uint64_t)i * p;
            if (v > limit || p > lp[i]) break;
            lp[(uint32_t)v] = p;
            if (p == lp[i]) {
                exp[(uint32_t)v] = exp[i] + 1;
                tau[(uint32_t)v] = (uint16_t)(tau[i] / (exp[i] + 1) * (exp[i] + 2));
                break;
            } else {
                exp[(uint32_t)v] = 1;
                tau[(uint32_t)v] = (uint16_t)(tau[i] * 2);
            }
        }
    }

    uint64_t record = 0;
    std::vector<uint32_t> solutions;
    for (uint32_t n = 1; n <= limit; ++n) {
        if (n > 1) {
            uint32_t m = n - 1;
            uint64_t val = (uint64_t)m + tau[m];
            if (val > record) record = val;
        }
        if (record <= (uint64_t)n + 2) solutions.push_back(n);
    }

    std::cout << "limit " << limit << "\nsolutions";
    for (uint32_t n : solutions) std::cout << " " << n;
    std::cout << "\n";

    record = 0;
    std::cout << "records\n";
    for (uint32_t m = 1; m < limit; ++m) {
        uint64_t val = (uint64_t)m + tau[m];
        if (val > record) {
            record = val;
            std::cout << m << " " << (uint32_t)tau[m] << " " << val << "\n";
        }
    }
    return 0;
}
