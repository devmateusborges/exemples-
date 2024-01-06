import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const UtilStore = createSlice({
  name: "util",

  initialState: {
    textloading: "",
  },
  reducers: {
    textloadingAction(state, action: PayloadAction<any>) {
      state.textloading = action.payload;
    },
  },
});

export const { textloadingAction } = UtilStore.actions;

export default UtilStore.reducer;
