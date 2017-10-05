import PVT
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.family'] = 'fantasy'
mpl.rcParams['font.fantasy'] = 'Times New Roman'

def test4():
    # TODO тут надо сделать тест для расчета z фактора газа, чтобы в итоге выводился график Стендинга

    gas = PVT.GasGeneral()
    ys= []
    xs = np.arange(1, 300, 20)
    for p in xs:
        gas._calc_z_dranchuk(p, 20)
        ys.append(gas.z)
    plt.ylim(0, np.max(ys))
    plt.xlim(0, np.max(xs))
    plt.grid(True)
    plt.title('Сверхсжимаемость', color='black', family='fantasy')
    plt.xlabel('Давление, атм', color='black', family='fantasy')
    plt.ylabel('z-фактор', color='black', family='fantasy')
    plt.plot(xs, ys, 'b', linewidth=3)
    plt.show()

def test3():
    """
    test from ruslan

    :return:
    """
    """Временно сюда построитель графиков"""
    def pvt_plot(oil, p_0=1, p_n=300, dp=20, t_c=20):

        xy = create_plots(oil, p_0, p_n, dp, t_c, 'Газосодержание')
        subplot_pvt(xy, 0, 0, 10, 'Газосодержание', 'Rs, м3/м3', 'Давление, атм', 'b')

        xy = create_plots(oil, p_0, p_n, dp, t_c, 'Плотность')
        subplot_pvt(xy, 0, 1, 10, 'Плотность', 'r, кг/м3', 'Давление, атм', 'g')

        xy = create_plots(oil, p_0, p_n, dp, t_c, 'Объемный коэффициент нефти')
        subplot_pvt(xy, 6, 0, 0.3, 'Объемный коэффициент нефти', 'Bo, м3/м3', 'Давление, атм', 'r')

        xy = create_plots(oil, p_0, p_n, dp, t_c, 'Вязкость нефти')
        subplot_pvt(xy, 6, 1, 0.3, 'Вязкость нефти', 'm, сПз', 'Давление, атм', 'b')

        xy = create_plots(oil, p_0, p_n, dp, t_c, 'Сжимаемость нефти')
        subplot_pvt(xy, 12, 0, 0, 'Сжимаемость нефти', 'Со, 1/атм', 'Давление, атм', 'm')

        plt.show()

    def create_plots(oil, p_0, p_n, dp, t_c, title):
        ys = []
        xs = np.arange(p_0, p_n, dp)
        for p in xs:
            oil.calc(p, t_c)
            if title == 'Газосодержание': ys.append(oil.rs_m3m3)
            if title == 'Плотность': ys.append(oil.rho_kgm3)
            if title == 'Объемный коэффициент нефти': ys.append(oil._bo_m3m3)
            if title == 'Вязкость нефти': ys.append(oil._mu_cp)
            if title == 'Сжимаемость нефти': ys.append(oil._co_1atm)
        return xs, ys

    def subplot_pvt(xy, a, b, dy, title, ylabel, xlabel, col):
        ax = plt.subplot2grid((16, 2), (a, b), rowspan=4, colspan=1)
        x, y = xy
        plt.ylim(0, np.max(y) + dy)
        plt.xlim(0, np.max(x))
        plt.grid(True)
        plt.title(title, color='black', family='fantasy')
        plt.xlabel(xlabel, color='black', family='fantasy')
        plt.ylabel(ylabel, color='black', family='fantasy')
        plt.plot(x, y, col, linewidth=3)
    oil = PVT.OilGeneral()
    pvt_plot(oil)


def test2():
    g = PVT.GasGeneral()
    print(g.pseudo_pressure_mpa)


def test1():
    a = PVT.OilGeneral()
    a.calc(230, 59)
    print(a.rs_m3m3)

    pp = np.arange(1, 300, 20)
    rs = []
    for p in pp:
        a.calc(p, 20)
        rs.append(a.rs_m3m3)
    plt.plot(pp, rs)
    plt.show()


# test3()
test4()