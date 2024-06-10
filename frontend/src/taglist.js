

const tagList = (prop) => {
  return (
      <>
          <div style={{display: "flex"}}>
              <input
                  type="checkbox"
                  id="checkbox"
                  checked={prop.finished}
                  onChange={() => {handleChange(prop.finished, prop.allTask, prop.setTask, prop.id, prop.setRefresh)}}
              />
              <div className={"taskcontent " + (prop.finished?"finished":"notfinished")}>
                  {prop.content}
              </div>  
              <button className="submit" onClick={()=>deleteElement(prop.id, prop.allTask, prop.setTask, prop.setRefresh)}> delete tasks </button>
          </div>
      </>
  );
}

export default tagList;