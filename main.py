import os
import re
import datetime
import json
import sys


class Graph:
    def __init__(self, nodes, links):
        self.nodes = nodes
        self.links = links


class GraphNode:
    def __init__(self, name, component = 1):
        self.name = name
        self.component = component


class GraphLink:
    def __init__(self, source, target, value=1):
        self.source = source
        self.target = target
        self.value = value


class Result:
    def __init__(self, name, description, visualTags, entity, timestamp, content):
        self.name = name
        self.description = description
        self.visualTags = visualTags
        self.entity = entity
        self.timestamp = timestamp
        self.content = content


def groupByImports(rootFolder, outputFile, extension='.java'):
    importsDict = {}
    classesDict = {}
    resultsDict = {}

    for root, dirs, files in os.walk(rootFolder):
        for file in files:
            if file.endswith(extension):
                with open(os.path.join(root, file), encoding='utf8') as f:
                    file_content = f.read()
                    imports = re.findall('import (.*?);', file_content)
                    classes = re.findall('class (\w*)', file_content)

                    for _import in imports:
                        formatted_output = _import.replace("static ", "")
                        importsDict.setdefault(formatted_output, []).append(os.path.join(root, file))

                    for _class in classes:
                        if _class:
                            classesDict.setdefault(os.path.join(root, file), []).append(_class)

    for key, value in importsDict.items():
        _import = key.split('.')[-1]
        for classesDictKey, classesDictValue in classesDict.items():
            if _import in classesDictValue:
                resultsDict.setdefault(classesDictKey, value)

    nodes = []
    links = []

    for key, value in resultsDict.items():
        parentNode = GraphNode(key)
        nodes.append(parentNode)
        for file in value:
            childNode = GraphNode(file)
            links.append(GraphLink(parentNode.name, childNode.name))
            nodes.append(childNode)

    _timestamp = str(datetime.datetime.now())
    graph = Graph(nodes, links)
    result = Result(
        name = 'CES - Imports Relations Graph',
        description = 'This is a plugin that show the relations between files based on the imports of each file',
        entity = 'MODULES',
        visualTags=["digraph", "hierarchical-edge-bundle", "forced-layered-graph"],
        content = graph,
        timestamp = 1614706330775
    )

    json_string = json.dumps(result, default=lambda o: o.__dict__, indent=4)

    f = open(outputFile, 'w')
    f.write('[')
    f.write(json_string)
    f.write(']')
    f.close


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Invalid number of arguments!")
        print("Try: py main.py {rootFolder} {outPutFile}")
        exit(1)

    groupByImports(sys.argv[2], sys.argv[1])
