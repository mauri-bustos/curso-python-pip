import matplotlib.pyplot as plot

'''
plot.plot([1, 2, 3, 4],[1, 4, 9, 16])

plot.ylabel('y numbers')
plot.xlabel('x numbers')

plot.savefig('pie.png')
plot.close()
'''

def generate_bar_charts(name, labels, values):
    fig, ax = plot.subplots()
    ax.bar(labels, values)
    plot.savefig(f'./imgs/{name}.png')
    plot.close()

def generate_pie_charts(labels, values):
    fig, ax = plot.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plot.savefig('pie.png')
    plot.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 40, 55]
    #generate_bar_charts(labels, values)
    generate_pie_charts(labels, values)