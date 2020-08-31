#!/usr/bin/env python3

"""Example usage of the pyalgo lib.

Run from ALGO root directory.
"""

__author__ = 'Ronja Schnur'
__email__ = 'rschnur@students.uni-mainz.de'

from pyalgo import (
    QuadraticSpline,
    QuadraticSplineModel,
    Simulation,
    PhotonLoader,
    DefaultPhotonGenerator,
    Intervall,
    EllipticModel
)
import math
import numpy
import time
from tools import falke, parabola

def main():
    #generator = PhotonLoader('test/tube.out')  # load input data
    a = numpy.arange(0, 121, 1)
    b = numpy.arange(50, 600, 50)
    out_string = ""
    #use default photon generator - currently implements a point light source
    #implement a modified version in CUDA code if you want to modify the light source
    #Parameters are
    #nPhotons, sigma, lx, ly, lz, seed
    #{lx, ly, lz} defines light position, seed is optional
    #b is the scattering length
    a_list =[]
    efficiency_list =[]
    for j in range(len(b)):
        for i in range(len(a)):
            out_string = ""
            generator = DefaultPhotonGenerator(1000000, 0, 0, 100, a[i])
            generator.generate()
            #length, a_inner, b_inner, alpha_inner, x_inner, y_inner, a_outer, b_outer, alpha_outer
            model = EllipticModel(120, 4.3, 4.3, 0, 0, 0, 4.5, 4.5, 0)
            #model, n1, n2, lambda_abs, lambda_sc, generator
            simulation = Simulation(model, 1.49, 1.0, 200, b[j], generator)
            start = time.time()
            result = simulation.simulateData()
            end = time.time()
            print(end-start)
            count = 0
            for p in range(1000000):
                if((result[1][p][1]<=1.5707) and ((result[2][p] == 1) or (result[2][p] == 65))):
                    count+=1
            efficiency_list.append(count/10000)

        a_list.append(efficiency_list)

        with open("output_flomas_data1_abs_const_sc" + str(b[j])+ ".csv", "w") as out_file: 
            for m in range(len(a)):
                out_string = ""
                out_string += str(efficiency_list[m]) + "\n"
                out_file.write(out_string)
        efficiency_list = []
    print(a_list) 

    #do stuff with result now
    #print(result)
    #result is tuple with
    #([x,y,z] <- np.array, [phi, theta, dt] <- np.array, exit_code <- np.array, detected <- int) ?
    #numpy.save('data/tout.npy', result)
    #print(result[3])

             
   
    


if __name__ == '__main__':
    main()
