#include <stdio.h>
#include <string.h>
#define N 200010

char s[N];
char t[N];

int a[1000];
int p[100];
int tot;

bool z[20010];
bool x[300];
bool y[300];

int ne[N];

int main() {
    int n;
    int flag;
    int ans;
    for (int i = 2; i < 200; i ++){
        if (a[i] == 0)
            p[tot ++] = i;
        for (int j = 0; j < tot && p[j] * i < 200; j ++){
            a[p[j] * i] = 1;
            if (i % p[j] == 0)
                break;
        }
    }

    while(scanf("%d", &n) != EOF){
        tot = 0;
        flag = 0;
        memset(x ,0, sizeof(x));
        memset(y ,0, sizeof(y));
        memset(z ,0, sizeof(z));
        scanf("%s", s); 
        scanf("%s", t); 
        for (int i = 0; i < n; i ++){
            if (s[i] != t[i]) 
                ne[tot++] = i;
        }
        for (int i = 0; i < tot; i ++){
            if (z[p[s[ne[i]] % 32] * p[t[ne[i]] % 32]]){
                flag = 2;
                ans = i;
                break;
            } else if (x[p[s[ne[i]] % 32]]){
                flag = 1;
                ans = i;
                x[p[t[ne[i]] % 32]] = 1;
            } else if (y[p[t[ne[i]] % 32]]){
                flag = 1;
                ans = i;
                y[p[s[ne[i]] % 32]] = 1;
            }
            z[p[s[ne[i]] % 32] * p[t[ne[i]] % 32]] = 1;
        }
        for (int i = 0; i < tot; i ++){
            if (flag == 2){
                if (p[s[ne[i]] % 32] * p[t[ne[i]] % 32] == p[s[ne[ans] % 32]] * p[t[ne[ans] % 32]]){
                    printf("%d\n%d %d\n", tot - 2, i, ans); 
                    break;
                }
            } else if (flag == 1){
                //if ()
            }
            else {
                break;
            }
        }
    }
    return 0;
}
