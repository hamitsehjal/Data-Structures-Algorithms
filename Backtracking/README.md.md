How to avoid duplicates?
1. When we have distince numbers, simply use the trick of always keeping record the index from where we want to start the iteration
2. If we allow duplicate elements, then we need to avoid picking the same element as it will result in similar combinations. In that case, in addition to above, we also need to do the following:
	 - sort the input
	 - avoid similar element twice. Simply do the check if `if j > i
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NzUxODM4MDJdfQ==
-->