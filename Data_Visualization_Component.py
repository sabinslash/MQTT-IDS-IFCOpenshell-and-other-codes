
import * as OBC from "openbim-components";
   import MQTT from "mqtt"
   export class DataVisualizationComponent extends OBC.Component<string>
     implements OBC.UI {
     enabled = true;
     uiElement = new OBC.UIElement<{
       topToolbar: OBC.SimpleUIComponent;
       dataWindow: OBC.FloatingWindow;
       main: OBC.Button;
}>();
     constructor(components: OBC.Components) {
       super(components);
       this.enabled = true;
       const sensorb = new OBC.Button(components);
       this.sensorButton = sensorb;
       sensorb.materialIcon = "sensors_off";
       sensorb.tooltip = "Sensors";
       sensorb.onClick.add(() =>
           { if (!this.mqttConnectionExists) {
                this.establishConnection();
                this.setUI();
                this.dataWindow.visible = true;
                sensorb.materialIcon = "sensors";
             } else {
                this.terminateConnection();
                this.dataWindow.visible = false;
                sensorb.materialIcon = "sensors_off";
} });
       this.uiElement.set({ main: sensorb });
     }
sensorButton: OBC.Button;
// mqttBroker = "mqtt://xrdevmqtt.edu.metropolia.fi:1883"
mqttBroker = "ws://localhost:9001/mqtt" ;
  topic = "#";
  mqttClient: MQTT.Client;
  mqttConnectionExists = false;
  
  establishConnection() {
     this.mqttClient = MQTT.connect(this.mqttBroker);
     this.mqttConnectionExists = true;
     this.mqttClient.on("connect", () => {
       this.mqttClient.subscribe(this.topic, (err) => {
         if (!err) {
            this.mqttClient.publish("presence", "Ok");
         } else {
           console.log("Error in connect:", err)
}}); });
     this.mqttClient.on("message", (topic, msg) => {
       console.log("Topic:", topic, "Value:", msg.toString())
});
     this.mqttClient.on("error", (err) => {
        console.log("On error:", err)
}); }
  terminateConnection() {
     this.mqttClient.end()
     this.mqttConnectionExists = false;
}
  dataWindow: OBC.FloatingWindow;
  setUI() {
    const topToolbar = new OBC.SimpleUIComponent(this.components);
    const dataw = new OBC.FloatingWindow(this.components);
    this.dataWindow = dataw;
    this.components.ui.add(dataw);
    dataw.title = "Real-time data";
    dataw.onHidden.add(() => (this.sensorButton.active = false));
    dataw.onVisible.add(() => (this.sensorButton.active = true));
    dataw.description = "description";
    dataw.visible = true;
    this.uiElement.set({
      topToolbar: topToolbar,
      dataWindow: dataw,
      main: this.sensorButton
      });
      }}

