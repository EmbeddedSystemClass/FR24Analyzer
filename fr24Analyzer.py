from FR24Analyzer import FR24Analyzer
from FR24Analyzer.fit import fit
import time
import argparse

parser = argparse.ArgumentParser(description='Approach time analyzer with respect to FR24 data. Run "get" for data gathering and "fit" to analye the existing data.')
parser.add_argument('-f','--fit', help='Fit Instance',required=False)
parser.add_argument('-g','--get',help='Get Instance', required=False)
parser.add_argument('-l','--log', help='Logging to log file.', required=False)
args = parser.parse_args()

if __name__ == "__main__":
    #Ugly but fast fix for issue #7 - Make logging optional issue
    logOption = False
    if args.log != None:
        logOption = True
    else:
        logOption = False

    analyzer = FR24Analyzer.FR24Analyzer(logging=logOption)
    if args.get != None:
        while True:
            analyzer.getLandingTimeToAirport()
            time.sleep(2)

    elif args.fit != None:
        fitter = fit.Fit()
        fitter.fitData()

    else:
        print("Usage: \n Get: python fr24Analyzer.py - g \n" +
              "Fit: python fr24Analyzer.py -f \n" + 
              "Logging: -l LOG")
