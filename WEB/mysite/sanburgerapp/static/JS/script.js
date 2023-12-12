/* Copyright 2023 The MediaPipe Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. */
import { MDCTextField } from "https://cdn.skypack.dev/@material/textfield";
import { TextClassifier, FilesetResolver } from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-text@0.10.0";
// Get the required elements
const submit = document.getElementById("send");
let array_preparadas=["¿QUE PASA AMIGO EN QUE PUEDO AYUDARTE?"];
let negativas=["VETE DE AQUI,NO QUEREMOS LLORONES","CON QUE ESAS TENEMOS,MIRA TUS ESPALDAS A PARTIR DE AHORA...",
        "MIRA NENE,EN BARRIO VACILO Y EN EL MIO MARCO ESTILO","ME DAN IGUAL TUS CRITICAS,MI MAMA ME DIJO UNA VEZ,APORTA O APARTAAAA",
        "TIENES SUERTE DE ESTAR AL OTRO LADO DE LA PANTALLA..."];
let positivas=["GRACIAS POR EL FEEDBACK,LLORANDO ESTOY TIO","POR GENTE COMO TU NOS DEDICAMOS A ESTO,INCREIBLE PANA","GRACIAS PAPI,NUNCA OLVIDARE ESTAS PALABRAS,DE VERDAD...","DA GUSTO RECIBIR ESTE FEEEDBACK,HAMBURGUESAS GRATIS PARA TODA LA VIDA PARA TI!"];
let historial_chat=[array_preparadas[0]];
const container=document.getElementById('history');
let textClassifier;
// Create the TextClassifier object upon page load
const createTextClassifier = async () => {
    const text = await FilesetResolver.forTextTasks("https://cdn.jsdelivr.net/npm/@mediapipe/tasks-text@0.10.0/wasm");
    textClassifier = await TextClassifier.createFromOptions(text, {
        baseOptions: {
            modelAssetPath: `https://storage.googleapis.com/mediapipe-models/text_classifier/bert_classifier/float32/1/bert_classifier.tflite`
        },
        maxResults: 5
    });
};
createTextClassifier();

// Add a button click listener that classifies text on click
submit.addEventListener("click", async () => {
    let input = document.getElementById("entered");
    historial_chat.push(input.value);
    if (input.value === "") {
        alert("Please write some text, or click 'Populate text' to add text");
        return;
    }
    let result = textClassifier.classify(input.value);
    input.value='';
    if(result.classifications[0].categories[0].categoryName=='positive'){
        historial_chat.push(positivas[Math.floor(Math.random() * positivas.length)]);
    }else if(result.classifications[0].categories[0].categoryName=='negative'){
        historial_chat.push(negativas[Math.floor(Math.random() * negativas.length)]);
    }

    displayClassificationResult();
});
function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}
// Iterate through the sentiment categories in the TextClassifierResult object, then display them in #output
function displayClassificationResult() {
    var index=0;
    let html_final='';
    for(const item of historial_chat){
        if(index==0){
            html_final+='<div class="chat-message clearfix"><div class="chat-message-content clearfix"><span class="chat-time">13:35</span><h5>MANUEL GARCES</h5><p>'+item+'</p></div></div>'
        }else{
            if(index%2==0){
                html_final+='<div class="chat-message clearfix"><div class="chat-message-content clearfix"><span class="chat-time">13:35</span><h5>MANUEL GARCES</h5><p>'+item+'</p></div></div>'
            }else{
                html_final+='<div class="chat-message clearfix"><div class="chat-message-content clearfix"><span class="chat-time">13:35</span><h5>USUARIO</h5><p>'+item+'</p></div></div>'
            }
        }
        index+=1;
    };
    container.innerHTML=html_final;
}