import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const PreferenceStore = createSlice({
  name: "preference",

  initialState: {
    dataGridState: {} as any,
  },
  reducers: {
    dataGridStateAction(state, action: PayloadAction<any>) {
      state.dataGridState[action.payload.key] = action.payload.state;
    },
  },
});

export const { dataGridStateAction } = PreferenceStore.actions;

export default PreferenceStore.reducer;
