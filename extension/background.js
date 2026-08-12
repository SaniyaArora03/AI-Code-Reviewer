chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "reviewCode",
    title: "Review With AI",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {

  if (info.menuItemId !== "reviewCode")
    return;

  const selectedCode = info.selectionText || "";

  console.log("NEW SELECTED CODE:");
  console.log(selectedCode);

  await chrome.storage.local.set({
    selectedCode: selectedCode
  });

  console.log("Saved selected code.");
});