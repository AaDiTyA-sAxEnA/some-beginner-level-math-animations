from manim import *
import networkx as nx

class ChangeGraphLayout(Scene):
    def construct(self):
        G = Graph([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5)],
                  layout={1: [-2, 0, 0], 2: [-1, 0, 0], 3: [0, 0, 0], 4: [1, 0, 0], 5: [2, 0, 0]}
                  )
        self.play(Create(G))
        self.play(G.animate.change_layout("circular"))
        self.wait()

nxgraph=nx.erdos_renyi_graph(12,0.6)

class ImportNetworkx(Scene):
    def construct(self):
        G = Graph.from_networkx(nxgraph, layout="spectral", layout_scale=3)
        self.play(Create(G))
        self.play(*[G[v].animate.move_to(5 * RIGHT * np.sin(ind / 5 * PI) +
                                        3 * UP * np.cos(ind / 5 * PI))
                    for ind, v in enumerate(G.vertices)])
        self.play(Uncreate(G))

class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(g[1].animate.move_to([1, 1, 0]),
                  g[2].animate.move_to([-1, 1, 0]),
                  g[3].animate.move_to([1, -1, 0]),
                  g[4].animate.move_to([-1, -1, 0]))
        self.wait()


class GraphAutoPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        autolayouts = ["spring", "circular", "kamada_kawai",
                       "planar", "random", "shell",
                       "spectral", "spiral"]
        graphs = [Graph(vertices, edges, layout=lt).scale(0.6)
                  for lt in autolayouts]
        r1 = VGroup(*graphs[:3]).arrange()
        r2 = VGroup(*graphs[3:6]).arrange()
        r3 = VGroup(*graphs[6:]).arrange()
        self.add(VGroup(r1, r2, r3).arrange(direction=DOWN))

class GraphManualPosition(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        lt = {1: [0, 0, 0], 2: [1, 1, 0], 3: [1, -1, 0], 4: [-1, 0, 0]}
        G = Graph(vertices, edges, layout=lt)
        self.add(G)

class LabeledModifiedGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        g = Graph(vertices, edges, layout="circular", layout_scale=3,
                  labels=True, vertex_config={7: {"fill_color": RED}},
                  edge_config={(1, 7): {"stroke_color": RED},
                               (2, 7): {"stroke_color": RED},
                               (4, 7): {"stroke_color": RED}})
        self.add(g)


class PartiteGraph(Scene):
    def construct(self):
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3])
        G.add_edges_from([(0, 2), (0,3), (1, 2)])
        graph = Graph(list(G.nodes), list(G.edges), layout="partite", partitions=[[0, 1]])
        self.play(Create(graph))

class LinearNN(Scene):
    def construct(self):
        edges = []
        partitions = []
        c = 0
        layers = [2, 3, 3, 2]  # the number of neurons in each layer

        for i in layers:
            partitions.append(list(range(c + 1, c + i + 1)))
            c += i
        for i, v in enumerate(layers[1:]):
                last = sum(layers[:i+1])
                for j in range(v):
                    for k in range(last - layers[i], last):
                        edges.append((k + 1, j + last + 1))

        vertices = np.arange(1, sum(layers) + 1)

        graph = Graph(
            vertices,
            edges,
            layout='partite',
            partitions=partitions,
            layout_scale=3,
            vertex_config={'radius': 0.20},
        )
        self.add(graph)

class Tree(Scene):
    def construct(self):
        G = nx.Graph()

        G.add_node("ROOT")

        for i in range(5):
            G.add_node("Child_%i" % i)
            G.add_node("Grandchild_%i" % i)
            G.add_node("Greatgrandchild_%i" % i)

            G.add_edge("ROOT", "Child_%i" % i)
            G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
            G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)

        self.play(Create(
            Graph(list(G.nodes), list(G.edges), layout="tree", root_vertex="ROOT")))


#class LogScalingExample(Scene):
#    def construct(self):
#        ax = Axes(
#            x_range=[0, 10, 1],
#            y_range=[-2, 6, 1],
#            tips=False,
#            axis_config={"include_numbers": True},
#            y_axis_config={"scaling": LogBase(custom_labels=True)},
#        )
#
#        # x_min must be > 0 because log is undefined at 0.
#        graph = ax.plot(lambda x: x ** 2, x_range=[0.001, 10], use_smoothing=False)
#        self.add(ax, graph)

from manim import *

class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
        )

        sin_func_1 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            color=BLUE,
        )

        sin_func_2 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            x_range=[-4, 4],
            color=GREEN,
        ).move_to([0, 1, 0])

        self.add(cos_func, sin_func_1, sin_func_2)

from manim import *

class GetAxisLabelsExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        axes = ThreeDAxes()
        labels = axes.get_axis_labels(
            Text("x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
        )
        self.add(axes, labels)

from manim import *

class DodecahedronScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=35 * DEGREES)
        obj = Dodecahedron()
        self.add(obj)


