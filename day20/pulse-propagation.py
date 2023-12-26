from collections import deque
from time import time
import re

def parseSignalInput():
    with open(inputFilePath, 'r') as f:
        fileContent = f.read()

    broadcasterDests = []
    modules = dict()
    conjuctionMod = []
    regex = re.compile('([%&]?)([a-zA-Z]+)\s+->\s+(.*)')
    for line in fileContent.split('\n'):
        matchObj = re.match(regex, line)
        moduleType = None

        moduleType, name, dests = matchObj.groups()
        dests = dests.split(', ')

        if moduleType == '':
            broadcasterDests = dests
        elif moduleType == '%':
            moduleType = flipFlop
            state = False
            modules[name] = (moduleType, dests, state)
        elif moduleType == '&':
            moduleType = conjunction
            state = dict()
            modules[name] = (moduleType, dests, state)
            conjuctionMod.append(name)

    cjInputModuleDict = dict()
    for moduleName, module in modules.items():
        _, dests, _ = module
        for dest in dests:
            if dest in conjuctionMod:
                if dest in cjInputModuleDict:
                    cjInputModuleDict[dest].append(moduleName)
                else:
                    cjInputModuleDict[dest] = [moduleName]

    for moduleName, inputModulesName in cjInputModuleDict.items():
        moduleType, dests, state = modules[moduleName]
        #print(dict.fromkeys(inputModulesName, low))
        modules[moduleName] = (moduleType, dests, dict.fromkeys(inputModulesName, low))


    return broadcasterDests, modules

def main():
    broadcasterDests, modules = parseSignalInput()

    #keep counting pulse low and high in below list
    pulseSignal = [0, 0]  
    
    for _ in range(iterations):
        pulseSignal[0] += 1
        storeInQueue = deque()

        for destinationModuleName in broadcasterDests:
            storeInQueue.append((low, broadCaster, destinationModuleName))

        while storeInQueue:
            pulse, sourceModuleName, destinationModuleName = storeInQueue.popleft()

            pulseSignal[pulse == high] += 1
            
            if destinationModuleName not in modules:
                continue

            moduleType, dests, state = destinationModule = modules[destinationModuleName]
            
            if moduleType == flipFlop:
                moduleState = state
                if pulse == low:
                    moduleState = not moduleState
                    modules[destinationModuleName] = (moduleType, dests, moduleState)
                    # check pulses
                    if moduleState:
                        for dest in dests:
                            storeInQueue.append((high, destinationModuleName, dest))
                    else:
                        for dest in dests:
                            storeInQueue.append((low, destinationModuleName, dest))
            elif moduleType == conjunction:
                mostRecentPulseDict = state
                mostRecentPulseDict[sourceModuleName] = pulse
                modules[destinationModuleName] = moduleType, dests, (mostRecentPulseDict)
                #print(destinationModuleName,moduleType,mostRecentPulseDict)
                if all(value == high for value in mostRecentPulseDict.values()):
                    for dest in dests:
                        storeInQueue.append((low, destinationModuleName, dest))
                else:
                    for dest in dests:
                        storeInQueue.append((high, destinationModuleName, dest))
    print(pulseSignal[0] * pulseSignal[1])


inputFilePath = r"C:\Users\user\python\adventOfCode\adventOfCode\day20\input-day20.txt"
iterations = 1000

flipFlop = "ff"  
conjunction = "cj"  
broadCaster = "bc"  
low = "L"
high = "H"

if __name__ == "__main__":
    start_time = time()
    main()
    print(f"time take about {time() - start_time:.4f} seconds")

#Part-2 ..
