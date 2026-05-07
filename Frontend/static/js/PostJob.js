document.getElementById("jobForm").addEventListener("submit", function(e) {
    e.preventDefault();
  
    let title = document.getElementById("title").value;
    let desc = document.getElementById("desc").value;
    let budget = document.getElementById("budget").value;
  
    let message = document.getElementById("message");
  
    if(title === "" || desc === "" || budget === "") {
      message.style.color = "red";
      message.innerText = "Please fill all fields!";
    } else {
      message.style.color = "gold";
      message.innerText = "Job posted successfully ✔";
  
      console.log({
        title: title,
        desc: desc,
        budget: budget
      });
  
      document.getElementById("jobForm").reset();
    }
  });