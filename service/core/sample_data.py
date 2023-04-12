request_body = {
    "request_version": "v1.0",
    "optimiser": {
        "name": "Knapsack Optimiser",
        "type": "zero-one",
        "version": "v1.0"
    },
    "fields": [
        {
            "capacity": 850,
            "values": [
                360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
                78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
                87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
                312
            ],
            "weights": [
                7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
                42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
                3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
            ]
        }
    ]
}

response_body = {
  "metadata": {
    "optimiser": {
      "name": "Knapsack Optimiser",
      "type": "zero-one",
      "version": "v1.0"
    }
  },
  "results": [
    {
      "total_value": 7534,
      "total_weight": 850,
      "values": [
        0,
        1,
        3,
        4,
        6,
        10,
        11,
        12,
        14,
        15,
        16,
        17,
        18,
        19,
        21,
        22,
        24,
        27,
        28,
        29,
        30,
        31,
        32,
        34,
        38,
        39,
        41,
        42,
        44,
        47,
        48,
        49
      ],
      "weights": [
        7,
        0,
        22,
        80,
        11,
        59,
        18,
        0,
        3,
        8,
        15,
        42,
        9,
        0,
        47,
        52,
        26,
        6,
        29,
        84,
        2,
        4,
        18,
        7,
        71,
        3,
        66,
        31,
        0,
        65,
        52,
        13
      ]
    }
  ]
}

odd_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "sample": {
                        "value": response_body
                    }
                }
            }
        }
    },
}
