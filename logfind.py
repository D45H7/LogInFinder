#!/usr/bin/python3.9
#
# Coded by EtcAug10
# Forked from https://tools.d4rk5idehacker.or.id
# Easy Code for learn

import requests,random

banner = """
#  ]     ]   ] ]     ]  ]  ]
# ]  ]  ]   ]   ]   ]     ]
#  ]  Login Page Finder ]  ]
# ]  by EtcAug10  ]   ]    ]
#   ]    ]   ] ]]    ]  ] ]
#  ]]  ]  ] ]    ]     ]   ]
"""

print(banner)
print("\n(!) Bruteforcing to catch Login page")
target = input("Target domain: ")
url = "https://tools.d4rk5idehacker.or.id/Scanner/starting.php?str="+target
hasil = requests.get(url).text
print("\nMake result..")
open("hasil.html", "a").write(hasil)
print("\nFile saved in hasil.html")
quit("Busy here.. huh...")
