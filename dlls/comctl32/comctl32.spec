# Functions exported by the Win95 comctl32.dll
# (these need to have these exact ordinals, because some win95 dlls
#  import comctl32.dll by ordinal)
#   This list was created from a comctl32.dll v5.81 (IE5.01).

  2 stdcall MenuHelp(long long long long long long ptr)
  3 stdcall ShowHideMenuCtl(long long ptr)
  4 stdcall GetEffectiveClientRect(long long long)
  5 stdcall DrawStatusTextA(long ptr str long)
  6 stdcall CreateStatusWindowA(long str long long)
  7 stdcall CreateToolbar(long long long long long long ptr long)
  8 stdcall CreateMappedBitmap(long long long ptr long)
  9 stdcall -noname DPA_LoadStream(ptr ptr ptr long)
 10 stdcall -noname DPA_SaveStream(ptr ptr ptr long)
 11 stdcall -noname DPA_Merge(ptr ptr long ptr ptr long)
#12 stub Cctl1632_ThunkData32
 13 stdcall MakeDragList(long)
 14 stdcall LBItemFromPt(long long long long)
 15 stdcall DrawInsert(long long long)
 16 stdcall CreateUpDownControl(long long long long long long long long long long long long)
 17 stdcall InitCommonControls()
 71 stdcall -noname Alloc(long) COMCTL32_Alloc
 72 stdcall -noname ReAlloc(ptr long) COMCTL32_ReAlloc
 73 stdcall -noname Free(ptr) COMCTL32_Free
 74 stdcall -noname GetSize(ptr) COMCTL32_GetSize
151 stdcall -noname CreateMRUListA(ptr)
152 stdcall -noname FreeMRUList(long)
153 stdcall -noname AddMRUStringA(long str)
154 stdcall -noname EnumMRUListA(long long ptr long)
155 stdcall -noname FindMRUStringA(long str ptr)
156 stdcall -noname DelMRUString(long long)
157 stdcall -noname CreateMRUListLazyA(ptr long long long)
163 stub -noname CreatePage
164 stub -noname CreateProxyPage
167 stdcall -noname AddMRUData(long ptr long)
169 stdcall -noname FindMRUData(long ptr long ptr)
233 stdcall -noname Str_GetPtrA(str str long)
234 stdcall -noname Str_SetPtrA(str str)
235 stdcall -noname Str_GetPtrW(wstr wstr long)
236 stdcall -noname Str_SetPtrW(wstr wstr)
320 stdcall -noname DSA_Create(long long)
321 stdcall -noname DSA_Destroy(ptr)
322 stdcall -noname DSA_GetItem(ptr long long)
323 stdcall -noname DSA_GetItemPtr(ptr long)
324 stdcall -noname DSA_InsertItem(ptr long long)
325 stdcall -noname DSA_SetItem (ptr long long)
326 stdcall -noname DSA_DeleteItem(ptr long)
327 stdcall -noname DSA_DeleteAllItems(ptr)
328 stdcall -noname DPA_Create(long)
329 stdcall -noname DPA_Destroy(ptr)
330 stdcall -noname DPA_Grow(ptr long)
331 stdcall -noname DPA_Clone(ptr ptr)
332 stdcall -noname DPA_GetPtr(ptr long)
333 stdcall -noname DPA_GetPtrIndex(ptr ptr)
334 stdcall -noname DPA_InsertPtr(ptr long ptr)
335 stdcall -noname DPA_SetPtr(ptr long ptr)
336 stdcall -noname DPA_DeletePtr(ptr long)
337 stdcall -noname DPA_DeleteAllPtrs(ptr)
338 stdcall -noname DPA_Sort(ptr ptr long)
339 stdcall -noname DPA_Search(ptr ptr long ptr long long)
340 stdcall -noname DPA_CreateEx(long long)
341 stdcall -noname SendNotify(long long long ptr) COMCTL32_SendNotify
342 stdcall -noname SendNotifyEx(long long long ptr long) COMCTL32_SendNotifyEx
350 stdcall -noname StrChrA(str str) COMCTL32_StrChrA
351 stdcall -noname StrRChrA(str str long) COMCTL32_StrRChrA
352 stdcall -noname StrCmpNA(str str long) COMCTL32_StrCmpNA
353 stdcall -noname StrCmpNIA(str str long) COMCTL32_StrCmpNIA
354 stdcall -noname StrStrA(str str) COMCTL32_StrStrA
355 stdcall -noname StrStrIA(str str) COMCTL32_StrStrIA
356 stdcall -noname StrCSpnA(str str) COMCTL32_StrCSpnA
357 stdcall -noname StrToIntA(str) COMCTL32_StrToIntA
358 stdcall -noname StrChrW(wstr long) COMCTL32_StrChrW
359 stdcall -noname StrRChrW(wstr wstr long) COMCTL32_StrRChrW
360 stdcall -noname StrCmpNW(wstr wstr long) COMCTL32_StrCmpNW
361 stdcall -noname StrCmpNIW(wstr wstr long) COMCTL32_StrCmpNIW
362 stdcall -noname StrStrW(wstr wstr) COMCTL32_StrStrW
363 stdcall -noname StrStrIW(wstr wstr) COMCTL32_StrStrIW
364 stdcall -noname StrSpnW(wstr wstr) COMCTL32_StrSpnW
365 stdcall -noname StrToIntW(wstr) COMCTL32_StrToIntW
366 stub -noname StrChrIA
367 stub -noname StrChrIW
368 stub -noname StrRChrIA
369 stub -noname StrRChrIW
372 stub -noname StrRStrIA
373 stub -noname StrRStrIW
374 stub -noname StrCSpnIA
375 stub -noname StrCSpnIW
376 stub -noname IntlStrEqWorkerA
377 stub -noname IntlStrEqWorkerW
382 stdcall -noname SmoothScrollWindow(ptr)
383 stub -noname DoReaderMode
384 stub -noname SetPathWordBreakProc
385 stdcall -noname DPA_EnumCallback(long long long)
386 stdcall -noname DPA_DestroyCallback(ptr ptr long)
387 stdcall -noname DSA_EnumCallback(ptr ptr long)
388 stdcall -noname DSA_DestroyCallback(ptr ptr long)
389 stub -noname SHGetProcessDword
390 stub -noname ImageList_SetColorTable
400 stdcall -noname CreateMRUListW(ptr)
401 stdcall -noname AddMRUStringW(long wstr)
402 stdcall -noname FindMRUStringW(long wstr ptr)
403 stdcall -noname EnumMRUListW(long long ptr long)
404 stdcall -noname CreateMRUListLazyW(ptr long long long)
410 stdcall SetWindowSubclass(long ptr long long)
411 stdcall GetWindowSubclass(long ptr long ptr)
412 stdcall RemoveWindowSubclass(long ptr long)
413 stdcall DefSubclassProc(long long long long)
414 stub -noname MirrorIcon
415 stdcall -noname DrawTextWrap(long long long long long)
416 stub -noname DrawTextExPrivWrap
417 stdcall -noname ExtTextOutWrap(long long long long ptr wstr long ptr)
418 stub -noname GetCharWidthWrap
419 stdcall -noname GetTextExtentPointWrap(long long long long)
420 stub -noname GetTextExtentPoint32Wrap
421 stub -noname TextOutWrap

# Functions imported by name

@ stdcall CreatePropertySheetPage(ptr) CreatePropertySheetPageA
@ stdcall CreatePropertySheetPageA(ptr)
@ stdcall CreatePropertySheetPageW(ptr)
@ stdcall CreateStatusWindow(long str long long) CreateStatusWindowA
@ stdcall CreateStatusWindowW(long wstr long long)
@ stdcall CreateToolbarEx(long long long long long long ptr long long long long long long)
@ stdcall DestroyPropertySheetPage(long)
@ stdcall DllGetVersion(ptr) COMCTL32_DllGetVersion
@ stdcall DllInstall(long ptr) COMCTL32_DllInstall
@ stdcall DrawStatusText(long ptr ptr long) DrawStatusTextA
@ stdcall DrawStatusTextW(long ptr wstr long)
@ stdcall FlatSB_EnableScrollBar (long long long)
@ stdcall FlatSB_GetScrollInfo (long long ptr)
@ stdcall FlatSB_GetScrollPos (long long)
@ stdcall FlatSB_GetScrollProp (long long ptr)
@ stdcall FlatSB_GetScrollRange (long long ptr ptr)
@ stdcall FlatSB_SetScrollInfo (long long ptr long)
@ stdcall FlatSB_SetScrollPos (long long long long)
@ stdcall FlatSB_SetScrollProp (long long long long)
@ stdcall FlatSB_SetScrollRange (long long long long long)
@ stdcall FlatSB_ShowScrollBar (long long long)
@ stdcall GetMUILanguage()
@ stdcall ImageList_Add(ptr long long)
@ stdcall ImageList_AddIcon(ptr long)
@ stdcall ImageList_AddMasked(ptr long long)
@ stdcall ImageList_BeginDrag(ptr long long long)
@ stdcall ImageList_Copy(ptr long ptr long long)
@ stdcall ImageList_Create(long long long long long)
@ stdcall ImageList_Destroy(ptr)
@ stdcall ImageList_DragEnter(long long long)
@ stdcall ImageList_DragLeave(long)
@ stdcall ImageList_DragMove(long long)
@ stdcall ImageList_DragShowNolock(long)
@ stdcall ImageList_Draw(ptr long long long long long)
@ stdcall ImageList_DrawEx(ptr long long long long long long long long long)
@ stdcall ImageList_DrawIndirect(ptr)
@ stdcall ImageList_Duplicate(ptr)
@ stdcall ImageList_EndDrag()
@ stdcall ImageList_GetBkColor(ptr)
@ stdcall ImageList_GetDragImage(ptr ptr)
@ stdcall ImageList_GetFlags(ptr)
@ stdcall ImageList_GetIcon(ptr long long)
@ stdcall ImageList_GetIconSize(ptr ptr ptr)
@ stdcall ImageList_GetImageCount(ptr)
@ stdcall ImageList_GetImageInfo(ptr long ptr)
@ stdcall ImageList_GetImageRect(ptr long ptr)
@ stdcall ImageList_LoadImage(long str long long long long long) ImageList_LoadImageA
@ stdcall ImageList_LoadImageA(long str long long long long long)
@ stdcall ImageList_LoadImageW(long wstr long long long long long)
@ stdcall ImageList_Merge(ptr long ptr long long long)
@ stdcall ImageList_Read(ptr)
@ stdcall ImageList_Remove(ptr long)
@ stdcall ImageList_Replace(ptr long long long)
@ stdcall ImageList_ReplaceIcon(ptr long long)
@ stdcall ImageList_SetBkColor(ptr long)
@ stdcall ImageList_SetDragCursorImage(ptr long long long)
@ stdcall ImageList_SetFilter(ptr long long)
@ stdcall ImageList_SetFlags(ptr long)
@ stdcall ImageList_SetIconSize(ptr long long)
@ stdcall ImageList_SetImageCount(ptr long)
@ stdcall ImageList_SetOverlayImage(ptr long long)
@ stdcall ImageList_Write(ptr ptr)
@ stdcall InitCommonControlsEx(ptr)
@ stdcall InitMUILanguage(long)
@ stdcall InitializeFlatSB(long)
@ stdcall PropertySheet(ptr) PropertySheetA
@ stdcall PropertySheetA(ptr)
@ stdcall PropertySheetW(ptr)
@ stdcall UninitializeFlatSB(long)
@ stdcall _TrackMouseEvent(ptr)
