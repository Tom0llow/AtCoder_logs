N = int(input())
# DP �z���p�ӂ���
# �{��ł� i ���ڂ̓���Ƃ��āuA�����v�uB�����v�uC�����v��3�ʂ肪�l������
# ���ꂼ��̍s�������邽�߂̍ő�K���x�����ꂼ��̑Q�����ŋ��߂�
# i ���ڂ� A�AB�AC ����邽�߂̍ő�K���x�� dp[i][0]�Adp[i][1]�Adp[i][2] �Ƃ���
dp = [[0]*3 for _ in range(N+1)]

# �������������
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1, N+1):
    a, b, c = map(int, input().split())
    dp[i][0] = max(dp[i-1][1]+a, dp[i-1][2]+a)
    dp[i][1] = max(dp[i-1][0]+b, dp[i-1][2]+b)
    dp[i][2] = max(dp[i-1][0]+c, dp[i-1][1]+c)

# for d in dp:
#     print(d)

ans = max(dp[-1])
print(ans)
