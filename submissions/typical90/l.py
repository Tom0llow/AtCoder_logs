from collections import defaultdict

class UnionFind():
    """
    Union Find�؃N���X

    Attributes
    --------------------
    n : int
        �v�f��
    root : list
        �؂̗v�f��
        0�����ł���΂��̃m�[�h�����ł���A�Y���̒l���v�f��
    rank : list
        �؂̐[��
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            �v�f��
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        �m�[�hx�̍���������

        Parameters
        ---------------------
        x : int
            ������m�[�h

        Returns
        ---------------------
        root : int
            ���̃m�[�h
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        �؂̕���

        Parameters
        ---------------------
        x : int
            ���������m�[�h
        y : int
            ���������m�[�h
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        �����O���[�v�ɑ����邩����

        Parameters
        ---------------------
        x : int
            ���肵���m�[�h
        y : int
            ���肵���m�[�h

        Returns
        ---------------------
        ans : bool
            �����O���[�v�ɑ����Ă��邩
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        �؂̃T�C�Y���v�Z

        Parameters
        ---------------------
        x : int
            �v�Z�������؂̃m�[�h

        Returns
        ---------------------
        size : int
            �؂̃T�C�Y
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        ���̃m�[�h���擾

        Returns
        ---------------------
        roots : list
            ���̃m�[�h
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        �O���[�v�����擾

        Returns
        ---------------------
        size : int
            �O���[�v��
        """
        return len(self.roots())

    def group_members(self):
        """
        �S�ẴO���[�v���Ƃ̃m�[�h���擾

        Returns
        ---------------------
        group_members : defaultdict
            �����L�[�Ƃ����m�[�h�̃��X�g
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    

H,W = map(int,input().split())
Q = int(input())

G = UnionFind(H*W+1)
M = [-1] * (H*W+1)


def check(n,x):
    if M[x] == 1 and M[n] == 1:
        G.unite(n,x)


for _ in range(Q):
    q = list(map(int,input().split()))
    
    if q[0] == 1:
        r,c = q[1:]
        n = W*(r-1) + (c-1)
        M[n] = 1

        if n-W >= 0:                    check(n,n-W)    # ���Ƃ̊֌W
        if n+W < H*W:                   check(n,n+W)    # ���Ƃ̊֌W 
        if n%W != 0 and n-1 >= 0:       check(n,n-1)    # ���Ƃ̊֌W
        if (n+1)%W != 0 and n+1 < H*W:  check(n,n+1)    # ���Ƃ̊֌W
            
    else:
        ra,ca,rb,cb = q[1:] 
        n1 = W*(ra-1) + ca-1
        n2 = W*(rb-1) + cb-1

        if G.same(n1,n2) and M[n1] == M[n2] == 1:   print('Yes')
        else:   print('No')
