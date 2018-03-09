import os
import ftputil
from hurry.filesize import size

total=0

top_levels=[]

with ftputil.FTPHost(os.environ['HOST'], os.environ['USER'], os.environ['PASS']) as host:
    for level in top_levels:
        for root, dirs, files in host.walk(level):
            for name in files:
                target=host.path.join(root, name)
                print(target, "=", size(host.path.getsize(target)))
                total=total+host.path.getsize(target)

print("Total=",size(total))

