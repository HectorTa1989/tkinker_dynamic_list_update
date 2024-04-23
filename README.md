# tkinker dynamic list update

## Problem:

Need to make 2 dropdown lists. The first one has 5-7 items. When selecting one of those items, the content of the second dropdown list changes. But how to change it requires calling a calculation function based on a list of arbitrary input parameters, so the content of the items in the list is unknown in advance. Need to make it change dynamically by calling the function to create a list for dropdown2.

## Solution:

We use ttk.Combobox to create a dropdown list. The function compute_dropdown2_options calculates the content of the second dropdown based on the value of the first dropdown. The update_dropdown2 function is called every time the value of the first dropdown changes to update the content of the second dropdown.

**Change the dynamic and call the function to create a list for dropdown 2:**

When the user changes the selection in the first dropdown (dropdown1), the <> event is fired. We have assigned this event to the update_dropdown2() function using dropdown1.bind("<>", update_dropdown2).

The update_dropdown2() function is called every time the first dropdown changes.

In the update_dropdown2() function, we get the current value of the first dropdown (dropdown1.get()) and use it to call the compute_dropdown2_options() function to calculate the content for the second dropdown (dropdown2). Then we update the content of the second dropdown by setting dropdown2['values'] to the new list of options.

**Update the content of dropdown 2:**

In the update_dropdown2() function, we update the contents of the second dropdown (dropdown2) by setting dropdown2['values'] to the new list of options, computed from the compute_dropdown2_options() function.

Thus, by calling the update_dropdown2() function when the first dropdown changes, we ensure that the content of the second dropdown will be dynamically updated based on the first dropdown's selection.
