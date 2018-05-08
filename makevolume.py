#! python 2
import vtk

class makevolume:
	
	def __init__(self):
		self.volumecolorTransferFunction = vtk.vtkColorTransferFunction()
		self.isocolorTransferFunction = vtk.vtkColorTransferFunction()
		self.opacityTransferFunction = vtk.vtkPiecewiseFunction()
		self.isocolor = vtk.vtkColorTransferFunction()
		self.volumeProperty = vtk.vtkVolumeProperty()
		self.volume = vtk.vtkVolume()
		self.volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
		self.actor = vtk.vtkActor()

		self.isomapperlist = []


	
	def volumeopacity(self, valuelist, opacitylist):
		ops = zip(valuelist, opacitylist)
		for each in ops:
			self.opacityTransferFunction.AddPoint(each[0], each[1])
	
	def volumecolortransfer(self, value, rgbtuple):
		colors = zip(value, rgbtuple)
		for each in colors:
			rgb = each[1]
			self.volumecolorTransferFunction.AddRGBPoint(each[0], rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)

	def isocolortransfer(self, value, rgbtuple):
		colors = zip(value, rgbtuple)
		for each in colors:
			rgb = each[1]
			self.isocolorTransferFunction.AddRGBPoint(each[0], rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)

	def createvolumeproperties(self, ambient, diffuse, specular):
		self.volumeProperty.SetScalarOpacity(self.opacityTransferFunction)
		self.volumeProperty.SetColor(self.volumecolorTransferFunction)
		self.volumeProperty.ShadeOn()
		self.volumeProperty.SetInterpolationTypeToLinear()
		self.volumeProperty.SetAmbient(0.4)
		self.volumeProperty.SetDiffuse(0.6)
		self.volumeProperty.SetSpecular(0.2)

	def generateisosurface(self, value, opacity, dataport):

		contour = vtk.vtkContourFilter()
		contour.SetInputConnection(dataport)
		contour.SetValue(0, value)
		
		mapper = vtk.vtkPolyDataMapper()
		mapper.SetInputConnection(contour.GetOutputPort())
		mapper.SetLookupTable(self.isocolorTransferFunction)
		self.actor.SetMapper(mapper)
		self.actor.GetProperty().SetOpacity(opacity)
		return self.actor
	
	
	def mapvolume(self, dataport):
		self.volumeMapper.SetInputConnection(dataport)
		self.volume.SetMapper(self.volumeMapper)
		self.volume.SetProperty(self.volumeProperty)
		return self.volume
