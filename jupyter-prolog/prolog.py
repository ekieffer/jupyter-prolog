from IPython.core.magic import Magics, magics_class, line_cell_magic
from jupyter_client.kernelspec import KernelSpecManager
from datetime import datetime
import os
import sys
import ipykernel
import json

@magics_class
class Prolog_Magics(Magics):

    @line_cell_magic
    def prolog(self, line, cell=None):
         if cell is None:
             content = line
         else:
             content = cell
         template='#!/bin/bash -l \n {custom} \n exec "$@"'
         conn_file = ipykernel.get_connection_file()
         # Get current kernel name
         with open(os.path.join(conn_file), 'r') as f:
             kernel_spec = json.load(f)
             kernel_id=kernel_spec['kernel_name']
         ksm = KernelSpecManager()
         current_specs = ksm.get_kernel_spec(kernel_id)
         with open(os.path.join(current_specs.resource_dir,'start.sh'),'w')as f:
              script=template.format(custom=content)    
              f.write(script)
         os.chmod(os.path.join(current_specs.resource_dir,'start.sh'),700)
         # Modify the kernel spec if needed
         with open(os.path.join(current_specs.resource_dir, 'kernel.json'), 'r+',encoding='utf-8') as f:
             kernel_spec = json.load(f)
             kernel_spec['argv'] = ["{resource_dir}/start.sh",sys.executable,"-m", "ipykernel_launcher",
                                                                             "-f", "{connection_file}"]
             kernel_spec['modified']=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
             f.seek(0)
             json.dump(kernel_spec, f,ensure_ascii=False, indent=4)
             f.truncate()
         get_ipython().kernel.do_shutdown(True)

