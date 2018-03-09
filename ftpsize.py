import os
import sys
import ftputil
from hurry.filesize import size

total=0

top_levels=sys.argv[1:]

with ftputil.FTPHost(os.environ['HOST'], os.environ['USER'], os.environ['PASS']) as host:
    for level in top_levels:
        for root, dirs, files in host.walk(level):
            for name in files:
                target=host.path.join(root, name)
                print("{0:>7s} {1:s}".format(size(host.path.getsize(target)),target))
                total=total+host.path.getsize(target)

print("{0:>7s} TOTAL".format(size(total)))

