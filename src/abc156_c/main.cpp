#include <iostream>
#include <vector>

using namespace std;

typedef long long   ll;
typedef long double ld;

#define rep(i, n)      for (int i = 0; i < (int)(n); ++i)
#define rep3(i, m, n)  for (int i = (m); i < (int)(n); ++i)
#define rrep(i, n)     for (int i = (int)(n)-1; i >= 0; --i)
#define rrep3(i, m, n) for (int i = (int)(n)-1; i >= (m); --i)

#define endl '\n'
#define INF  0x7f7f7f7f7f7f7f7f
#define INFi 0x7f7f7f7f


ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }

ld average(const std::vector<ll> &X) {
  ll sum = 0;
  for (auto x: X) {
    sum += x;
  }
  return (ld)sum / X.size();
}

ll solve(int N, const std::vector<ll> &X) {
  ld ave = average(X);
  ll point = ll(ave+0.5);

  ll ans = 0;
  for (auto x: X) {
    ans += (x - point) * (x - point);
  }

  return ans;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int N;
  std::cin >> N;
  std::vector<ll> X(N);
  rep (i, N) {
    std::cin >> X[i];
  }

  auto ans = solve(N, X);
  std::cout << ans << '\n';

  return 0;
}
