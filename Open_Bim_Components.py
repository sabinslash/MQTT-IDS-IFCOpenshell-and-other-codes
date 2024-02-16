
import * as OBC from "openbim-components"
import * as THREE from "three"
import { GUI } from 'dat.gui'
import * as DVC from "./DataVisualizationComponent"

const viewer = new OBC.Components()
viewer.onInitialized.add(() => {})
viewer.scene = new OBC.SimpleScene(viewer)
const scene = viewer.scene.get()
const ambientLight = new THREE.AmbientLight(0xE6E7E4, 1)
const directionalLight = new THREE.DirectionalLight(0xF9F9F9, 0, 75)
directionalLight.position.set(10, 50, 10)
scene.add(ambientLight, directionalLight)
scene.background = new THREE.Color("#202932")
const viewerContainer = document.getElementById("app") as HTMLDivElement
const rendererComponent = new
OBC.PostproductionRenderer(viewer, viewerContainer)
viewer.renderer = rendererComponent
viewer.init()
viewer.camera = new OBC.OrthoPerspectiveCamera(viewer)
viewer.raycaster = new OBC.SimpleRaycaster(viewer)
rendererComponent.postproduction.enabled = true

new OBC.SimpleGrid(viewer, new THREE.Color(0x666666))

const highlighter = new OBC.FragmentHighlighter(viewer)
highlighter.setup()
const propertiesProcessor = new
OBC.IfcPropertiesProcessor(viewer)
const hider = new OBC.FragmentHider(viewer);
await hider.loadCached();
const gui = new GUI();
const entitiesGui = gui.addFolder("Classes");

const ifcLoader = new OBC.FragmentIfcLoader(viewer)
ifcLoader.onIfcLoaded.add(async (model) => {
const classifier = new OBC.FragmentClassifier(viewer);
classifier.byEntity(model);
const classifications = classifier.get();
const classes = {};
const classNames = Object.keys(classifications.entities);
for (const name of classNames) {
       classes[name] = true;
}
for (const name in classes) {
  entitiesGui.add(classes, name).onChange(async (visible)=> {
    const found = await classifier.find({entities:[name]});
    hider.set(visible, found);});}

    propertiesProcessor.process(model)
    await highlighter.update()
    highlighter.events.select.onHighlight.add((selection) => {
        const fragmentID = Object.keys(selection)[0]
        const expressID = Number([...selection[fragmentID]][0])
        console.log(selection, fragmentID, expressID)
        propertiesProcessor.renderProperties(model, expressID);
    })})
    const mainToolbar = new OBC.Toolbar(viewer)
    mainToolbar.addChild(
      ifcLoader.uiElement.get("main"),
      propertiesProcessor.uiElement.get("main"),
      hider.uiElement.get("main"))
      viewer.ui.addToolbar(mainToolbar)

      const dataVisualizer = new DVC.DataVisualizationComponent(viewer)
      mainToolbar.addChild(dataVisualizer.uiElement.get("main"))
      
