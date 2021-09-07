import { observable, autorun, action, makeObservable, computed } from 'mobx';
import { createContext } from 'react';
class Store {
  users = ['adi', 'yosi']

  constructor() {
    makeObservable(this, {
      users: observable,
      inc: action,
      sum: computed
    })
  }

  inc(stat) {
    this.user[stat]++
  }

  get sum() {
    return 5
  }

}

export const store = new Store();


