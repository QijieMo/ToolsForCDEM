import pymatgen as mg
from pymatgen.io.cif import CifWriter
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

def read_xyz(filename):
    xyz_file = open(filename,"r")
    xyz_data = xyz_file.readlines()
    if len(xyz_data[0].split())<2:
        xyz_data=xyz_data[2:]
    xyz_file.close()
    return  xyz_data

def read_cell(filename):
    cell_file = open(filename,"r")
    cell_data = cell_file.readlines()
    returndata = []
    for i in xrange(len(cell_data)):
        cell_data[i]=cell_data[i].split()
        for j in xrange(len(cell_data[i])):
            returndata.append(cell_data[i][j])
    cell_file.close()
    return returndata

def process_xyz(xyz):
    returndata = []
    at_namedata = []
    for i in xrange(len(xyz)):
        xyz[i]=xyz[i].split()
        at_namedata.append(xyz[i][0])
        xyz[i] = [float(xyz[i][1]),float(xyz[i][2]),float(xyz[i][3])]
    return xyz,at_namedata
    
def process_cell(cell):
    a=[float(cell[0]),float(cell[1]),float(cell[2])]
    b=[float(cell[3]),float(cell[4]),float(cell[5])]
    c=[float(cell[6]),float(cell[7]),float(cell[8])]
    returndata = [a,b,c]
    return returndata

def at_types_fromnamedata(at_namedata):
    at_types = []
    for x in xrange(len(at_namedata)):
        if at_namedata[x] not in at_types:
            at_types.append(at_namedata[x])
    return at_types


def pmg_xyz2cifFunc(xyzFilename,cell_file,sym_tol,cifFilename):
  xyz = read_xyz(xyzFilename)
  cell = read_cell(cell_file)
  #processing for conversion
  cell_processed = process_cell(cell)
  xyz_processed, at_namedata = process_xyz(xyz)
  st = mg.Structure(cell_processed,at_namedata,xyz_processed,coords_are_cartesian=True)
  finder = SpacegroupAnalyzer(st,symprec=sym_tol)
  returner = "Space Group "+ str(finder.get_space_group_number()) + "  "+finder.get_space_group_symbol()
  cifFile = CifWriter(st,symprec=sym_tol)
  cifFile.write_file(cifFilename)
  return returner,st.volume
