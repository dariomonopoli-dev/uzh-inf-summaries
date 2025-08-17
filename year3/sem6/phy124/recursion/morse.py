MORSE = {
    ".": {
        "label": "E",
        "children": {
            "-": {
                "label": "A",
                "children": {
                    "-": {
                        "label": "W",
                        "children": {
                            "-": {
                                "label": "J",
                                "children": {"-": {"label": "1", "children": {}}},
                            },
                            ".": {"label": "P", "children": {}},
                        },
                    },
                    ".": {
                        "label": "R",
                        "children": {".": {"label": "L", "children": {}}},
                    },
                },
            },
            ".": {
                "label": "I",
                "children": {
                    "-": {
                        "label": "U",
                        "children": {
                            ".": {"label": "F", "children": {}},
                            "-": {
                                "label": "",
                                "children": {"-": {"label": "2", "children": {}}},
                            },
                        },
                    },
                    ".": {
                        "label": "S",
                        "children": {
                            ".": {
                                "label": "H",
                                "children": {
                                    "-": {"label": "4", "children": {}},
                                    ".": {"label": "5", "children": {}},
                                },
                            },
                            "-": {
                                "label": "V",
                                "children": {"-": {"label": "3", "children": {}}},
                            },
                        },
                    },
                },
            },
        },
    },
    "-": {
        "label": "T",
        "children": {
            ".": {
                "label": "N",
                "children": {
                    ".": {
                        "label": "D",
                        "children": {
                            ".": {
                                "label": "B",
                                "children": {".": {"label": "6", "children": {}}},
                            },
                            "-": {"label": "X", "children": {}},
                        },
                    },
                    "-": {
                        "label": "K",
                        "children": {
                            ".": {"label": "C", "children": {}},
                            "-": {"label": "Y", "children": {}},
                        },
                    },
                },
            },
            "-": {
                "label": "M",
                "children": {
                    ".": {
                        "label": "G",
                        "children": {
                            "-": {"label": "Q", "children": {}},
                            ".": {
                                "label": "Z",
                                "children": {".": {"label": "7", "children": {}}},
                            },
                        },
                    },
                    "-": {
                        "label": "O",
                        "children": {
                            ".": {
                                "label": "",
                                "children": {".": {"label": "8", "children": {}}},
                            },
                            "-": {
                                "label": "",
                                "children": {
                                    ".": {"label": "9", "children": {}},
                                    "-": {"label": "0", "children": {}},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}


def getLabel(x):
    return x['label']


def getChildren(x):
    if 'children' not in x.keys(): # if x is a label
        return x
    return x['children']


def rec_Morsecode(code):
    code = code.split()
    if len(code) == 1:
        message = ""
        for part in code:
            currentMorse = None
            for i, signal in enumerate(part):
                if currentMorse is None:
                    currentMorse = MORSE[str(signal)]
                else:
                    currentMorse = currentMorse[str(signal)]
                if i == len(part) - 1:
                    currentMorse = getLabel(currentMorse)
                else:
                    currentMorse = getChildren(currentMorse)
            message = message + currentMorse
        return message
    else:
        ret_front = rec_Morsecode(code[0])
        ret_mes = rec_Morsecode(code[1:])
        return ret_front + ret_mes


print(rec_Morsecode("..-. .. -. -.. .. -. --."))
