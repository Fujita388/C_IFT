# atomsファイルを読み込んで、界面活性剤濃度を計算

with open("interface_tension.atoms", "r") as f:
    lines = f.readlines()
A = float(lines[2].split()[0])  # 全粒子数
B = float(lines[3].split()[0])  # Bond数
C = 100 * (B / (A - B))  # 濃度(%)
print(C)
