N, K = map(int, input().split())
h = list(map(int, input().split()))

# DP �z���p��
# dp[i] �ɂ� i �Ԗڂ̑���ɂ��ǂ蒅�����߂ɕK�v�ȍŒ�R�X�g������
dp = [0]*N

# �������������
dp[0] = 0

# �Q�����ɂ��������ă��[�v����
for i in range(1, N):
    # i �����݂��鑫��ƍl����
    # i �Ԗڂ̑���֍s�����@�� max(K, i-K) �ʂ肠��
    # ���ꂼ��̐������ɂ�����R�X�g�� tmp (temporary) �ɂ܂Ƃ߂�
    tmp = []
    for j in range(max(0, i-K), i):
        tmp.append(abs(h[j]-h[i]) + dp[j])
    # tmp �̂����ŏ��R�X�g�� dp[i] �Ƃ���
    # print(tmp)
    dp[i] = min(tmp)

# dp �z��̖����� N �Ԗڂ̑���ɒH�蒅�����߂ɕK�v�ȃR�X�g�ƂȂ�
# print(dp)
print(dp[-1])
