#! python 2

from windows import window
from makevolume import makevolume
import vtk


def createrendering(filename, volumeval, volumeopacities, volumecolors, volumecolorvalues,
					isoctf, isovcolorvals, isovals, isoopacity, depthpeel = False, roi = False, extractedroi = None):
	
	if(roi == True):
		read = extractedroi
	elif(roi == False):
		read = vtk.vtkDataSetReader()
		read.SetFileName(filename)
	volumelist = []
	isosurfacelist = []
	volume = makevolume()
	
	values = volumeval
	opacities = volumeopacities
	if (len(volumeval)!= 0):
		volume.volumeopacity(values, opacities)
		colval = volumecolors
		rgb = volumecolorvalues
		volume.volumecolortransfer(colval, rgb)
		volume.createvolumeproperties(0.4, 0.6, 0.2)
		volumelist.append(volume.mapvolume(read.GetOutputPort()))
	
	isocolv  = isoctf
	isorgb = isovcolorvals
	
	volume.isocolortransfer(isocolv, isorgb)
	isovalueandopacitylist = zip(isovals,isoopacity)
	for each in isovalueandopacitylist:
		isosurfacelist.append(volume.generateisosurface(each[0], each[1],read.GetOutputPort()))
	
	newWindow = window(isosurfacelist, volumelist)
	newWindow.createWindow(depthpeel, roi)



mrcp = {'filename': 'mrcp.vtk',
		  'volumeval':  [2042.37, 4066.5, 7130.05, 11561.6, 13348.3],
		  'volumeopacities':  [ 0, 1],
		  'volumecolors': [1312.95, 3902.38, 7184.75],
		  'volumecolorvalues': [(220, 195, 172), (204, 153, 102), (172, 204, 135)],
		  'isoctf': [],
		  'isovcolorvals': [],
		  'isovals': [],
		  'isoopacity': [],
		  'depthpeel': False }

contrastcombined = {'filename': 'fatsat.vtk',
		  'volumeval': [500, 800, 1734],
		  'volumeopacities': [0, .2,0],
		  'volumecolors': [2221, 2336, 3550],
		  'volumecolorvalues': [(220, 195, 172), (204, 153, 102), (172, 204, 135)],
		  'isoctf': [0, 1734],
		  'isovcolorvals': [(59, 76, 192),(180, 4, 38)],
		  'isovals': [800],
		  'isoopacity': [0.5],
		  'depthpeel': True }

contrastvol = {'filename': 'fatsat.vtk',
		  'volumeval': [500, 800, 1734],
		  'volumeopacities': [0, 1,0],
		  'volumecolors': [2221, 2336, 3550],
		  'volumecolorvalues': [(220, 195, 172), (204, 153, 102), (172, 204, 135)],
		  'isoctf': [],
		  'isovcolorvals': [],
		  'isovals': [],
		  'isoopacity': [],
		  'depthpeel': True }

contrastiso = {'filename': 'fatsat.vtk',
		  'volumeval': [],
		  'volumeopacities': [],
		  'volumecolors': [],
		  'volumecolorvalues': [],
		  'isoctf': [0, 1734],
		  'isovcolorvals': [(204, 153, 102),(204, 153, 102)],
		  'isovals': [800],
		  'isoopacity': [0.8],
		  'depthpeel': True }

read = vtk.vtkDataSetReader()
read.SetFileName('isovis.vtk')
extract = vtk.vtkExtractVOI()
extract.SetVOI(0,500, 200,260,0,150)
extract.SetSampleRate(1, 1, 1)
extract.SetInputConnection(read.GetOutputPort())


fullbody = {'filename': None,
		  'volumeval': [-22.66, -15.69, -4.20, 40.12, 86.07, 254.15],
		  'volumeopacities': [0, .19, 0.7, 0, 0,0.83 ],
		  'volumecolors': [42.90,163.49, 277.64],
		  'volumecolorvalues': [(140, 67, 30), (234, 160, 30), (255, 255, 255)],
		  'isoctf': [],
		  'isovcolorvals': [],
		  'isovals': [],
		  'isoopacity': [],
		  'depthpeel': False,
		  'roi': True,
		  'extractedroi': extract}

createrendering(**contrastcombined)
createrendering(**contrastvol)
createrendering(**contrastiso)
createrendering(**mrcp)
createrendering(**fullbody)
