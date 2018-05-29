from pymoo.algorithms.genetic_algorithm import GeneticAlgorithm
from pymoo.operators.crossover.bin_uniform_crossover import BinaryUniformCrossover
from pymoo.operators.crossover.real_simulated_binary_crossover import SimulatedBinaryCrossover
from pymoo.operators.mutation.bin_bitflip_mutation import BinaryBitflipMutation
from pymoo.operators.mutation.real_polynomial_mutation import PolynomialMutation
from pymoo.operators.sampling.bin_random_sampling import BinaryRandomSampling
from pymoo.operators.sampling.real_random_sampling import RealRandomSampling
from pymoo.operators.selection.random_selection import RandomSelection
from pymoo.operators.survival.reference_line_survival import ReferenceLineSurvival
from pymoo.util.reference_directions import get_ref_dirs_from_n


class NSGAIII(GeneticAlgorithm):
    def __init__(self, var_type, pop_size=100, verbose=1):

        if var_type == "real":
            super().__init__(
                pop_size=pop_size,
                sampling=RealRandomSampling(),
                selection=RandomSelection(),
                crossover=SimulatedBinaryCrossover(),
                mutation=PolynomialMutation(),
                survival=None,
                verbose=verbose
            )
        elif var_type == "binary":
            super().__init__(
                pop_size=pop_size,
                sampling=BinaryRandomSampling(),
                selection=RandomSelection(),
                crossover=BinaryUniformCrossover(),
                mutation=BinaryBitflipMutation(),
                survival=None,
                verbose=verbose,
                eliminate_duplicates=True
            )

        self.ref_lines = None

    def _initialize(self, problem):
        super()._initialize(problem)
        self.ref_lines = get_ref_dirs_from_n(problem.n_obj, self.pop_size)
        self.survival = ReferenceLineSurvival(self.ref_lines)