#! python 2
import vtk 


class window:
	def __init__(self, actorlist, volumelist):
		self.render = vtk.vtkRenderer()
		self.renWindow = vtk.vtkRenderWindow()
		self.renWindow.AddRenderer(self.render)
		self.interactor = vtk.vtkRenderWindowInteractor()
		self.interactor.SetRenderWindow(self.renWindow)
		self.actorstoadd = actorlist
		self.volumestoadd = volumelist
		self.t = vtk.vtkTransform()
		self.box = vtk.vtkBoxWidget()
		self.planes = vtk.vtkPlanes()
		self.clipper = vtk.vtkClipPolyData()
		self.selectMapper = vtk.vtkPolyDataMapper()
		self.selectActor = vtk.vtkLODActor()


	def createWindow(self, depthpeel = False, roi = False):
		if (self.actorstoadd != None):
			for each in self.actorstoadd:
				self.render.AddActor(each)
		if (self.volumestoadd != None):
			for each in self.volumestoadd:
				self.render.AddVolume(each)
		if(depthpeel == True):
			self.renWindow.SetAlphaBitPlanes(1)
			self.renWindow.SetMultiSamples(0)
			self.render.SetUseDepthPeeling(1)
			self.render.SetMaximumNumberOfPeels(100)
			self.render.SetOcclusionRatio(0.1)
		self.renWindow.SetSize(2000, 2000)
		self.renWindow.Render()
		self.interactor.Start()
