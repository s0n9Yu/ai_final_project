import { useState } from "react";

const URL = "http://127.0.0.1:5000/query"

const submit = async (text, setTags) => {
  if (text.length === 0) return
  console.log(text)

  const data = new URLSearchParams();
  data.append("query", text);

  const res = await fetch(URL, {
      method: 'POST',
      body: data,
  })
  console.log(res)
  const res_json = await res.json();
  console.log(res_json["result"])
  setTags(res_json["result"])
}

function App() {

  const [tags, setTags] = useState([])
  const [input, setInput] = useState("")

  return (
    <div className="App" >
       <textarea type="text" id="inputbox" onChange={(e) => setInput(e.target.value)} style={{width:"100%"}}></textarea>
       <button id="submit" onClick={()=> {submit(input, setTags)}}>submit</button>
       <ul class="horizontal-list"> 
       {
        tags.map((e) => {
          return (<a>#{e} </a> )
        })
       }
       </ul> 
    </div>
  );
}

export default App;
//       <input type="text" id="inputbox" onChange={(e) => setInput(e.target.value)}></input>
