# Project-4--Particle-Swarm-Optimization.
Particle Swarm Optimization using python.

# ABSTRACT:
 
 
The Particle Swarm Optimization (or famously known as the PSO algorithm), is a stochastic algorithm, based on the population of the subjects involved in the study. In this algorithm, the method recursively processes the inputs and positions of the particles or subjects, which are present in a large quantity to concatenate themselves on a desired common location through constant and repeated comparisons of certain measures within the group. This include the local- best position, which is the closest position of an individual object from the final location and global-best position, which is the position of the object closest to the destination. There are values and rules to be set before the application of this algorithm, which define the paths that the individual objects may take in order to achieve their common goal. This may include the distance one can cover, in what directions they can move and how much of each is to be done.

# INTRODUCTION:
Inspired from nature, the Particle Swarm Optimization algorithm was created after observing the common movement of a flock of birds in the search of food or during migration from one place to another. How they work in unity to find food for their group through common sharing of what they observe about their environments is a key part of this process. This concept of swarm intelligence presents a more reliable way of finding the most well-optimized solution for a specific problem. In this algorithm, the concept of swarm intelligence can be used to find the optimum solution for a problem in a large space. The algorithm uses the particle’s velocity and position to make them move around in the space. The objects use their own best positions and the global best positions to move around the space, which are updated as new overall best positions are found. This recursive process helps the objects to gradually move towards the optimum position in a non-linear fashion.

# PROGRAMMING DESIGN:

# Programming Language: 
Python
 
# Algorithm:
1.	Create objects or particles that will be used to find the optimum solution in the space.
2.	Decide every particle’s initial position using a reference function.
3.	If current position of the particle is better than its previous best position, then:
i.	Find the current value.
ii.	Update the particles local best position.
4.	Find the best particle position overall and set it as the global best position.
5.	Update the velocities of the particles using the search strategy.
Vk+1 i = WkVk i + c1r1(Pki - Xki) + c2r2(Pkg - Xki)
where the next velocity is determined by the inertia ‘w’, the locally best location of a particle ‘Pki’ and the globally best location among all particles ‘Pkg’
6.	Update the particles’ positions respectively using:
xk+1 i = xk i+vk+1
7.	If stopping condition is reached or maximum iterations are complete, then end the process.
8.	Else, repeat process from Step 2.


# Pseudocode:
1.	For each particle:
Initialize particle Pi
END
2.	Do:
A.	For each particle:
i.    Compare positions of Pi
ii. If Pi (Current position) > Pi (Best position):
Pi (Best Position) = Pi (Current Position)
END

B.	For each particle:
i.	Compare positions of all particles
ii.	Calculate velocities of particles using:
Vk+1 i = WkVk i + c1r1(Pki - Xki) + c2r2(Pkg - Xki)
iii.	Update new positions of particles using:
xk+1 i = xk i+vk+1
END
3.	While: Stopping condition is not reached or maximum iterations are not completed.


# Space Complexity:
The space complexity of the algorithm will be O(i), as ‘i’ particles will be initialized and will store coordinates of their positions.
 
# Time Complexity:
There is a for loop in the beginning of the process repeating ‘i’ times, where i is the number of particles. After that we see a do-while condition, which has the condition of either achieving stopping condition or completing maximum iterations. Since we consider the worst case, we assume that the condition will run for all iterations ‘n’. Now that do-while loop consists of two for loops each running ‘i’ times, so it becomes i raised to the power 2 or i2. So, our estimated time complexity becomes: O(i+ni2).


# CODE:
![Capture](https://user-images.githubusercontent.com/92660593/193565768-ba56947b-6e63-43ec-877b-d009bf41843a.PNG)


# EXPERIMENTAL SETUP:
We take multiple variations in the values of c1 and c2, where c1 is the confidence a particle has in itself or the local best and c2 is the confidence a particle has in its neighbors or the globally best position. Also, we take small variations in the total values of inertia of the particles in order to achieve our desired results. These changes in values present a wide range of results where the particles present different optimum positions and costs. Our code was able to graph the results using the matplotlib library. Some of the results are shown in the next chapter.
# RESULTS AND DISCUSSION:
![Capture1](https://user-images.githubusercontent.com/92660593/193565814-75bb28b4-460b-485f-a1aa-063861e04863.PNG)


# Example:
For c1 = 0.3, c2 = 0.5 and w = 0.9

![image](https://user-images.githubusercontent.com/92660593/193565871-a948effb-f826-4b28-9586-dcc610d5dc91.png)

![image](https://user-images.githubusercontent.com/92660593/193565895-30e61da1-c59d-4e0a-8085-48dbc86e77eb.png)
As we see all particles have collected on the best position represented by the collection of black dots.
 
# CONCLUSION:
The algorithm discussed above is one of the most used and reliable algorithms among scientists around the globe and can be used to solve a lot of optimization problems that may exist. It has been modified to fit other uses as well such as Hybridization, Gradient- based PSO algorithms, Alleviate premature convergence and others. Regardless, it also has its disadvantages as it is prone to fall in the local optimum in a large space and due to its recursive process, may have a convergence rate lower than other optimization algorithms.
# REFERENCES:
1.	Lec 8 : Particle Swarm Optimization (PSO) (January 2021): NPTEL IIT Guwahati:
Youtube.com https://www.youtube.com/watch?v=8dpYjgRskgQ
2.	Learn Particle Swarm Optimization (PSO) in 20 minutes (March 2018): Ali Mirjalli:
Youtube.com https://www.youtube.com/watch?v=JhgDMAm-imI
3.	Particle swarm optimization: Wikipedia.com
https://en.wikipedia.org/wiki/Particle_swarm_optimization#:~:text=In%20computational
%20science%2C%20particle%20swarm,a%20given%20measure%20of%20quality.
4.	D. Wang · D. Tan · L. Liu (2017): Particle swarm optimization algorithm: an overview.
DOI 10.1007/s00500-016-2474-6
