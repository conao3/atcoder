#include <iostream>

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

auto solve(int n, const std::vector<int64_t> &a) {
  // TODO: edit here
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  // failed to analyze input format
  // TODO: edit here
  int n;
  std::cin >> n;
  std::vector<ll> a(n);
  rep (i, n) {
    std::cin >> a[i];
  }

  auto ans = solve(n, a);
  // failed to analyze output format
  // TODO: edit here
  std::cout << ans << '\n';

  return 0;
}
