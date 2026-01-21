const form = document.getElementById("feedbackForm");
const responseMsg = document.getElementById("responseMsg");
const feedbackList = document.getElementById("feedbackList");
const loadBtn = document.getElementById("loadBtn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const feedbackData = {
    message: document.getElementById("message").value,
  };

  try {
    const res = await fetch("/submit-feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(feedbackData),
    });

    const data = await res.json();

    if (data.success) {
      responseMsg.style.color = "green";
      responseMsg.textContent = data.message;
      form.reset();
    } else {
      responseMsg.style.color = "red";
      responseMsg.textContent = data.message;
    }
  } catch (err) {
    responseMsg.style.color = "red";
    responseMsg.textContent = "Server error. Try again!";
  }
});
