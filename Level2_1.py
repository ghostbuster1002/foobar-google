def solution(l):
    def split2int(l):
        m = []
        vi = ['major', 'feature', 'minor']
        for ver in l:
            temp = ver.split('.')
            ver_det = {key: None for key in vi}
            for n, key in zip(temp, vi):
                ver_det[key] = int(n)
            m.append(ver_det.copy())
        return m
    def pack2list(l):
        fl = []
        for x in l:
            ver = ''
            for y in x:
                if (x[y] is not None):
                    ver += str(x[y]) + '.'
            fl.append(ver[:-1])
        return fl
    l2int = split2int(l)
    l2i_sor = sorted(l2int, key=lambda i: (i['major'], i['feature'], i['minor']))
    sol = pack2list(l2i_sor)
    return sol
