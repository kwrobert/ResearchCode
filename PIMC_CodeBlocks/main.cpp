//
//  main.cpp
//  HelloWorld
//
//  Created by Kyle Robertson on 7/3/14.
//  Copyright (c) 2014 ___BonerInc___. All rights reserved.
//

#include "math.h"
#include <iostream>
#include <blitz/array.h>

using namespace blitz;
using namespace std;

typedef TinyVector<double,3> dVec;
typedef TinyVector<int,3> iVec;

int NDIM = 3;

class LJHexPorePotential
{
public:
    LJHexPorePotential(double);
    ~LJHexPorePotential();
    void getBounds(double,double);
    double V(const dVec);
    dVec gradV(const double, const double);
    double grad2V(const dVec);
    Array<dVec,1> initialConfig(const int, const int);
private:
    double boundList [6]; //Array in which the bounds will be stored
    double t; //Side length of hexagon
    double TotalPotential; // Variable to which we will write the total potential
    double sectionOne,sectionTwo,sectionThree,sectionFour,sectionFive,sectionSix; //potential for each section
    double density;
    double sigma;
    double epsilon;

};

LJHexPorePotential::LJHexPorePotential (const double sidelength)
{
    t = sidelength;
    /* The density of microspheres in silicate glass */
	density = 0.05982; // atoms / angstrom^3
    /* LJ interaction parameters */
	epsilon = 43.48; 	// Kelvin
	sigma   = 27.6;	// angstroms. This seems way too large if we're looking at nanopores on the order of 10 nm
};

LJHexPorePotential::~LJHexPorePotential(){
};

double LJHexPorePotential::V(dVec rhat)
{
    double denom3, denom9, denom33, denom39, denom43, denom49, x, y;
    x = rhat[0];
    y = rhat[1];
    getBounds(x, y);
    x = x/sigma;
    y = y/sigma; //Make x and y dimensionfull
    denom3 = pow(sqrt(3)*x+y-sqrt(3)*t,3);
    denom9 = pow(sqrt(3)*x+y-sqrt(3)*t,9);

    sectionOne = M_PI*(((-441*cos(boundList[0]))/(128*denom9)) + ((3*cos(boundList[0]))/(8*denom3)) - ((49*cos(3*boundList[0]))/(32*denom9))
                 +(cos(3*boundList[0])/(12*denom3)) - ((63*cos(5*boundList[0]))/(320*denom9)) + ((9*cos(7*boundList[0]))/(256*denom9))
                 +((7*cos(9*boundList[0]))/(1152*denom9)) + ((441*cos(boundList[1]))/(128*denom9)) - ((3*cos(boundList[1]))/(8*denom3))
                 +((49*cos(3*boundList[1]))/(32*denom9)) - (cos(3*boundList[1])/(12*denom3)) + ((63*cos(5*boundList[1]))/(320*denom9))
                 -((9*cos(7*boundList[1]))/(256*denom9)) - ((7*cos(9*boundList[1]))/(1152*denom9)) + ((441*sqrt(3)*sin(boundList[0]))/(128*denom9))
                 -((3*sqrt(3)*sin(boundList[0]))/(8*denom3)) - ((63*sqrt(3)*sin(5*boundList[0]))/(320*denom9)) - ((9*sqrt(3)*sin(7*boundList[0]))/(256*denom9))
                 -((441*sqrt(3)*sin(boundList[1]))/(128*denom9))+((3*sqrt(3)*sin(boundList[1]))/(8*denom3)) + ((63*sqrt(3)*sin(5*boundList[1]))/(320*denom9))
                 +((9*sqrt(3)*sin(7*boundList[1]))/(256*denom9)));

    sectionTwo = M_PI*(((9*cos(boundList[1])-cos(3*boundList[1])-9*cos(boundList[2])+cos(3*boundList[2]))/(12*pow(2*y-sqrt(3)*t,3))) - ((39690*cos(boundList[1])
                 -8820*cos(3*boundList[1]) + 2268*cos(5*boundList[1]) - 405*cos(7*boundList[1]) + 35*cos(9*boundList[1]) - 39690*cos(boundList[2])
                 +8820*cos(3*boundList[2]) - 2268*cos(5*boundList[2]) + 405*cos(7*boundList[2]) - 35*cos(9*boundList[2]))/(5760*pow(2*y-sqrt(3)*t,9))));

    denom33 = pow(sqrt(3)*(x+t)-y, 3);
    denom39 = pow(sqrt(3)*(x+t)-y, 9);

    sectionThree = M_PI*(((-3*cos(boundList[2]))/(8*denom33)) + ((441*cos(boundList[2]))/(128*denom39)) - (cos(3*boundList[2])/(12*denom33))
                   + ((49*cos(3*boundList[2]))/(32*denom39)) + ((63*cos(5*boundList[2]))/(320*denom39)) - ((9*cos(7*boundList[2]))/(256*denom39))
                   - ((7*cos(9*boundList[2]))/(1152*denom39)) + ((3*cos(boundList[3]))/(8*denom33)) - ((441*cos(boundList[3]))/(128*denom39))
                   + (cos(3*boundList[3])/(12*denom33)) - ((49*cos(3*boundList[3]))/(32*denom39)) - ((63*cos(5*boundList[3]))/(320*denom39))
                   + ((9*cos(7*boundList[3]))/(256*denom39)) + ((7*cos(9*boundList[3]))/(1152*denom39)) - ((3*sqrt(3)*sin(boundList[2]))/(8*denom33))
                   + ((441*sqrt(3)*sin(boundList[2]))/(128*denom39)) - ((63*sqrt(3)*sin(5*boundList[2]))/(320*denom39))
                   - ((9*sqrt(3)*sin(7*boundList[2]))/(256*denom39)) + ((3*sqrt(3)*sin(boundList[3]))/(8*denom33))- ((441*sqrt(3)*sin(boundList[3]))/(128*denom39))
                   + ((63*sqrt(3)*sin(5*boundList[3]))/(320*denom39)) + ((9*sqrt(3)*sin(7*boundList[3]))/(256*denom39)));

    denom43 = pow(sqrt(3)*(x+t)+y,3);
    denom49 = pow(sqrt(3)*(x+t)+y,9);

    sectionFour = M_PI*(((3*cos(boundList[3]))/(8*denom43)) - ((441*cos(boundList[3]))/(128*denom49)) + (cos(3*boundList[3])/(12*denom43))
                  - ((49*cos(3*boundList[3]))/(32*denom49)) - ((63*cos(5*boundList[3]))/(320*denom49)) + ((9*cos(7*boundList[3]))/(256*denom49))
                  + ((7*cos(9*boundList[3]))/(1152*denom49)) - ((3*cos(boundList[4]))/(8*denom43)) + ((441*cos(boundList[4]))/(128*denom49))
                  - (cos(3*boundList[4])/(12*denom43)) + ((49*cos(3*boundList[4]))/(32*denom49)) + ((63*cos(5*boundList[4]))/(320*denom49))
                  - ((9*cos(7*boundList[4]))/(256*denom49)) - ((7*cos(9*boundList[4]))/(1152*denom49)) - ((3*sqrt(3)*sin(boundList[3]))/(8*denom43))
                  + ((441*sqrt(3)*sin(boundList[3]))/(128*denom49)) - ((63*sqrt(3)*sin(5*boundList[3]))/(320*denom49))
                  - ((9*sqrt(3)*sin(7*boundList[3]))/(256*denom49)) + ((3*sqrt(3)*sin(boundList[4]))/(8*denom43)) - ((441*sqrt(3)*sin(boundList[4]))/(128*denom49))
                  + ((63*sqrt(3)*sin(5*boundList[4]))/(320*denom49)) + ((9*sqrt(3)*sin(7*boundList[4]))/(256*denom49)));

    sectionFive = M_PI*(((9*cos(boundList[4])-cos(3*boundList[4])-9*cos(boundList[5])+cos(3*boundList[5]))/(12*pow(2*y+sqrt(3)*t,3))) - ((39690*cos(boundList[4])
                  -8820*cos(3*boundList[4]) + 2268*cos(5*boundList[4]) - 405*cos(7*boundList[4]) + 35*cos(9*boundList[4]) - 39690*cos(boundList[5])
                  +8820*cos(3*boundList[5]) - 2268*cos(5*boundList[5]) + 405*cos(7*boundList[5]) - 35*cos(9*boundList[5]))/(5760*pow(2*y+sqrt(3)*t,9))));

    sectionSix = (M_PI/11520)*(((480*(9*cos(boundList[0]) + 2*cos(3*boundList[0]) - 9*cos(boundList[5]) - 2*cos(3*boundList[5]) + 9*sqrt(3)*(sin(boundList[0])
                  - sin(boundList[5]))))/pow(sqrt(3)*x-y-sqrt(3)*t,3)) + (1/pow(sqrt(3)*t+y-sqrt(3)*x,9))*(39690*cos(boundList[0]) + 17640*cos(3*boundList[0])
                  + 2268*cos(5*boundList[0]) - 405*cos(7*boundList[0]) - 70*cos(9*boundList[0]) + 70*cos(9*boundList[5]) - 9*(4410*cos(boundList[5])
                  + 1960*cos(3*boundList[5]) + 9*(28*cos(5*boundList[5]) - 5*cos(7*boundList[5]) + sqrt(3)*(28*sin(5*boundList[0])-490*sin(boundList[0])
                  + 5*sin(7*boundList[0]) + 490*sin(boundList[5]) - 28*sin(5*boundList[5]) - 5*sin(7*boundList[5]))))));

    TotalPotential = 4*epsilon*pow(sigma,3)*density*(sectionOne + sectionTwo + sectionThree + sectionFour + sectionFive + sectionSix);

    return TotalPotential;
};

void LJHexPorePotential::getBounds(double x, double y)
{
    boundList[0] = atan2(-y,(t-x));
    boundList[1] = atan2(((sqrt(3)/2)*t-y),((t/2)-x));
    boundList[2] = atan2(((sqrt(3)/2)*t-y),((-t/2)-x));
    boundList[3] = atan2(-y,(-(t+x)));
    boundList[4] = 2*M_PI + atan2(((-sqrt(3)/2)*t-y),((-t/2)-x));
    boundList[5] = 2*M_PI + atan2(((-sqrt(3)/2)*t-y),((t/2)-x));

};

dVec LJHexPorePotential::gradV(double x, double y)
{
    return 0.0;
};

double grad2V(const dVec)
{
    return 0.0;
};

Array<dVec,1> LJHexPorePotential::initialConfig(const Container *boxPtr, const int numParticles)
{
    Array<dVec,1> initialPos(numParticles);
	initialPos = 0.0;

	/* We shift the radius inward to account for the excluded volume from the
	 * hard wall.  This represents the largest prism that can be put
	 * inside a cylinder. */
	dVec lside;
	lside[0] = lside[1] = sqrt(2.0)*(t-1.0);
	lside[2] = boxPtr->side[NDIM-1];

	/* Get the linear size per particle */
	double initSide = pow((1.0*numParticles/product(lside)),-1.0/(1.0*NDIM));

	/* We determine the number of initial grid boxes there are in
	 * in each dimension and compute their size */
	int totNumGridBoxes = 1;
	iVec numNNGrid;
	dVec sizeNNGrid;

	for (int i = 0; i < NDIM; i++) {
		numNNGrid[i] = static_cast<int>(ceil((lside[i] / initSide) - EPS));

		/* Make sure we have at least one grid box */
		if (numNNGrid[i] < 1)
			numNNGrid[i] = 1;

		/* Compute the actual size of the grid */
		sizeNNGrid[i] = lside[i] / (1.0 * numNNGrid[i]);

		/* Determine the total number of grid boxes */
		totNumGridBoxes *= numNNGrid[i];
	}

	/* Now, we place the particles at the middle of each box */
	PIMC_ASSERT(totNumGridBoxes>=numParticles);
	dVec pos;
	for (int n = 0; n < totNumGridBoxes; n++) {

		iVec gridIndex;
		for (int i = 0; i < NDIM; i++) {
			int scale = 1;
			for (int j = i+1; j < NDIM; j++)
				scale *= numNNGrid[j];
			gridIndex[i] = (n/scale) % numNNGrid[i];
		}

		for (int i = 0; i < NDIM; i++)
			pos[i] = (gridIndex[i]+0.5)*sizeNNGrid[i] - 0.5*lside[i];

		boxPtr->putInside(pos);

		if (n < numParticles)
			initialPos(n) = pos;
		else
			break;
	}

	return initialPos;

};

int main()
{
    double value;
    Array<dVec,1> printarray;
    dVec positionVec;
    positionVec[0] = -1.0;
    positionVec[1] = -1.0;
    positionVec[2] = 0.0;

    LJHexPorePotential potentialObject = LJHexPorePotential(6);

    value = potentialObject.V(positionVec);
    printarray = potentialObject.initialConfig(2,2);

    cout << value;
    cout << "\n",
    cout << printarray;


};
