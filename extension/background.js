chrome.runtime.onInstalled.addListener(() => {

  chrome.contextMenus.create({
    id: "reviewCode",
    title: "Review With AI",
    contexts: ["selection"]
  });

});


chrome.contextMenus.onClicked.addListener(
  async (info, tab) => {

    if (info.menuItemId !== "reviewCode")
      return;

    const selectedCode =
      info.selectionText;

    chrome.storage.local.set({
      selectedCode
    });

  }
);