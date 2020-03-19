package com.lambdaschool.j52c2.services;

import com.lambdaschool.j52c2.models.Agent;
import com.lambdaschool.j52c2.models.Customer;
import com.lambdaschool.j52c2.models.Order;
import com.lambdaschool.j52c2.repos.OrderRepository;
import com.lambdaschool.j52c2.repos.AgentsRepository;
import com.lambdaschool.j52c2.repos.CustomersRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.persistence.EntityNotFoundException;
import java.util.ArrayList;
import java.util.List;

@Transactional
@Service(value="agentService")
public class AgentServiceImple {
    @Autowired
    private AgentRepository restrepos;

    @Override
    public List<Agent> findAll() {
        List<Agent> rtnList = new ArrayList<>();
        restrepos.findAll().iterator().forEachRemaining(rtnList::add);
        return rtnList;
    }

    @Override
    public Agent findAgentById(long id) {

        return restrepos.findById(id)
                .orElseThrow(()-> new EntityNotFoundException("ID = " + id));
    }

    @Override
    public Agent findAgentByName(String name) {
        Agent agent = restrepos.findByName(name);

        if(agent == null){
            throw new EntityNotFoundException("Agent not found, name = " + name);
        }
        return agent;
    }

    @Override
    public Agent findAgentByTelephone(String telephone) {
        Agent agent = restrepos.findByTelephone(telephone);

        if(agent == null){
            throw new EntityNotFoundException("Agent not found, telephone = " + telephone);
        }
        return agent;
    }

    @Override
    public Agent delete(long id) {
        if(restrepos.findById(id).isPresent()){
            restrepos.deleteById(id);
        }
        else {
            throw new EntityNotFoundException("ID = " + id);
        }
        return null;
    }

    @Transactional
    @Override
    public Agent save(Agent agent) {
        Agent newAgent = new Agent();
        newAgent.setName(agent.getName());
        newAgent.setAddress(agent.getAddress());
        newAgent.setCity(agent.getCity());
        newAgent.setState(agent.getState());
        newAgent.setTelephone(agent.getTelephone());

        // pointers
        // pointer gets set, all data goes away, doesn't bring info with it
        // newAgent.setMenus(agent.getMenus());

        for(Menu m : agent.getMenus()){
            newAgent.getMenus().add(new Menu(m.getDish(), m.getPrice(), newAgent));
        }
        return restrepos.save(newAgent);
    }

    @Transactional
    @Override
    public Agent update(Agent agent, long id) {

        Agent currentAgent =
                restrepos.findById(id)
                        .orElseThrow(()->new EntityNotFoundException(Long.toString(id)));

        if(agent.getName() != null){
            currentAgent.setName((agent.getName()));
        }
        if(agent.getAddress() != null){
            currentAgent.setAddress((agent.getAddress()));
        }
        if(agent.getCity() != null){
            currentAgent.setCity((agent.getCity()));
        }
        if(agent.getState() != null){
            currentAgent.setState((agent.getState()));
        }
        if(agent.getTelephone() != null){
            currentAgent.setTelephone((agent.getTelephone()));
        }
        if(agent.getMenus().size() > 0){
            for(Menu m : agent.getMenus()){
                currentAgent.getMenus().add(new Menu(m.getDish(), m.getPrice(), currentAgent));
            }

        }
        return restrepos.save(currentAgent);
    }
}
